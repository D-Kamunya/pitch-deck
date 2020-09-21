from . import db
from datetime import datetime

class User(db.Model):

    'User model schema'

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):

    'Pitch model schema'
    
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_body = db.Column(db.String)
    pitch_category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    votes = db.relationship('Vote',backref = 'pitch',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")

class Comment(db.Model):

    'Comment model schema'
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))

class Vote(db.Model):

    'Vote model schema'
    
    __tablename__ = 'votes'

    id = db.Column(db.Integer,primary_key = True)
    vote_type = db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))    

         