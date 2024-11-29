from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


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


class ModelDateDataMixin(Base):  # Mixin - клас функція якого розширити інші класи.
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    modified_at = Column(DateTime(timezone=True), default=datetime.utcnow)


class User(ModelDateDataMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(Text, nullable=False, default='/static/default_avatar/download.png')


class Post(ModelDateDataMixin):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    image = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    # user = relationship('User', backref='posts')


class Comment(ModelDateDataMixin):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    text = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    # user = relationship('user', backref='comments')
    # post = relationship('post', backref='comments')
