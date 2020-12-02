from ..database import db
from crypt import *

class Posts(db.Model):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.String(1500),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    feelings = db.relation("Feelings",backref="posts")
    events = db.relation("Events",backref="posts")

class Feelings(db.Model):
    __tablename__ = 'feelings'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    feeling = db.Column(db.String(30),nullable=False)

    post = db.relation("Posts")

class Events(db.Model):
    __tablename__ = 'events'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    event = db.Column(db.String(30),nullable=False)

    post = db.relation("Posts")