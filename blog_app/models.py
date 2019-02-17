from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')#u.posts, returns all the posts written by that user
    comments = db.relationship('Comment', backref = 'commenter', lazy = 'dynamic')#c.comments, returns all the comments written by that user

    def __repr__(self):
        return f'<User {self.username}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    body = db.Column(db.Text, nullable = False)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    image_file = db.Column(db.String(20), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#will return the user who wrote the post post.author
    comments = db.relationship('Comment', backref = 'posting', lazy = 'dynamic')#p.comments, returns all comments for that post

    def __repr__(self):
        return f'<Post {self.title}'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable = False)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#will return the user who wrote the comment comment.commenter
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))#will return the post that has the comment comment.posting



