import shutil
from pathlib import Path
from functools import wraps

from config import app, templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from db import get_db, User, Post, Favorite

from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Form, Depends, File, HTTPException
from pydantic import BaseModel


def login_required(view):
    @wraps(view)
    async def wrapped(request: Request, *args, **kwargs):
        if not request.session.get('is_authenticated', False):
            return RedirectResponse('/login', status_code=303)
        return await view(request, *args, **kwargs)
    return wrapped


def admin_required(view):
    @wraps(view)
    async def wrapped(request: Request, *args, **kwargs):
        if not request.session.get('is_admin', False):
            return RedirectResponse('/', status_code=303)
        return await view(request, *args, **kwargs)
    return wrapped


class FavoriteRequest(BaseModel):
    user_id: int
    post_id: int


@app.get('/', response_class=HTMLResponse)
@login_required
async def index(request: Request, db: Session = Depends(get_db)):
    post = db.query(Post).all()
    return templates.TemplateResponse('index.html', {'request': request, 'post': post})


@app.get('/registration', response_class=HTMLResponse)
async def register(request: Request,
                   is_invalid_data: bool = False):
    return templates.TemplateResponse('registration.html', {'request': request, 'is_invalid_data': is_invalid_data})


@app.post('/registration')
async def register(username: str = Form(),
                   password: str = Form(),
                   email: str = Form(),
                   db: Session = Depends(get_db)
                   ):
    user = User(username=username, password=password, email=email)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        return RedirectResponse('/registration?is_invalid_data=True', status_code=303)
    return RedirectResponse('/', status_code=303)


@app.get('/login', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@app.post('/login', response_class=HTMLResponse)
async def register(request: Request,
                   username: str = Form(),
                   password: str = Form(),
                   db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=username, password=password).first()
    if user is None:
        return RedirectResponse('/login')
    request.session['is_authenticated'] = True
    request.session['user_id'] = user.id
    request.session['is_admin'] = user.is_admin
    return RedirectResponse('/', status_code=303)


@app.get('/post-create', response_class=HTMLResponse)
@admin_required
async def profile(request: Request):
    return templates.TemplateResponse('post_create.html', {'request': request})


@app.post('/post-create')
@admin_required
async def create_post(request: Request,
                      title: str = Form(),
                      text: str = Form(),
                      short_text: str = Form(),
                      price: str = Form(),
                      img=File(),
                      db: Session = Depends(get_db)):
    save_image = Path(f'static/img/{img.filename}')
    with save_image.open("wb") as buffer:
        shutil.copyfileobj(img.file, buffer)

    new_post = Post(title=title,
                    text=text,
                    short_text=short_text,
                    image=f'/static/img/{img.filename}',
                    price=price,
                    user_id=request.session.get('user_id'))
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return RedirectResponse('/', status_code=303)


@app.get('/post-details/{post_id}')
@login_required
async def post_details(request: Request, post_id: int, db: Session = Depends(get_db)):
    current_post = db.query(Post).get(post_id)
    user = db.query(User).get(request.session['user_id'])
    return templates.TemplateResponse('post_details.html', {'request': request,
                                                            'current_post': current_post,
                                                            'user': user})


@app.post('/search')
async def search(search: str = Form(), db: Session = Depends(get_db)):
    search_post = db.query(Post).filter(Post.title.like(f"%{search}%")).all()
    return {'result': search_post}


@app.post('/add_to_favorites/')
def add_to_favorites(request: FavoriteRequest, db: Session = Depends(get_db)):
    favorite = db.query(Favorite).filter(Favorite.user_id == request.user_id,
                                         Favorite.post_id == request.post_id).first()
    if favorite:
        raise HTTPException(status_code=400, detail='Post is already in favorites')
    new_favorite = Favorite(user_id=request.user_id, post_id=request.post_id)
    db.add(new_favorite)
    db.commit()
    db.refresh(new_favorite)
    return {'message': 'Post added to favorites'}


@app.get('/profile', response_class=HTMLResponse)
@login_required
async def profile(request: Request, db: Session = Depends(get_db)):
    user = db.query(User).get(request.session['user_id'])
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    favorites = db.query(Favorite).filter(Favorite.user_id == user.id).all()
    favorite_posts = [{'id': fav.post.id,
                       'title': fav.post.title,
                       'short_text': fav.post.short_text,
                       'price': fav.post.price,
                       'image': fav.post.image, }for fav in favorites]
    return templates.TemplateResponse('profile.html', {'request': request,
                                                       'user': user,
                                                       'favorite_posts': favorite_posts})


@app.post('/post-details/{post_id}/edit-tour')
@login_required
async def edit_tour(request: Request,
                    post_id: int,
                    title: str = Form(),
                    text: str = Form(),
                    price: str = Form(),
                    db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    post.title = title
    post.text = text
    post.price = price
    db.commit()
    db.refresh(post)
    return {}


@app.post('/post-details/{post_id}/delete-tour')
@login_required
async def delete_tour(request: Request, post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return {'error': 'Post not found'}, 404

    favorites = db.query(Favorite).filter(Favorite.post_id == post_id).all()
    for favorite in favorites:
        db.delete(favorite)

    db.delete(post)
    db.commit()
    return {'success': 'Post deleted'}
