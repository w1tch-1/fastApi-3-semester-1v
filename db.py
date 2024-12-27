from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


DATABASE_URL = 'sqlite:///app.db'

engine = create_engine(DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(Text, nullable=False, default='/static/default_avatar/download.png')
    is_admin = Column(Boolean, nullable=True, default=False)

    favorites = relationship("Favorite", back_populates="user")


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    text = Column(String(4000), nullable=False)
    short_text = Column(String(120), nullable=False)
    price = Column(Integer, nullable=False)
    image = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    favorites = relationship("Favorite", back_populates="post")


class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    user = relationship("User", back_populates="favorites")
    post = relationship("Post", back_populates="favorites")
