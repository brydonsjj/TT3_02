from attr import has
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/socialmedia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)   
    name = db.Column(db.String(40), nullable=False, unique=True)
    age = db.Column(db.DateTime, nullable=False, unique=False)
    birthday = db.Column(db.String(40), nullable=False, unique=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(40), nullable=False, unique=False)
    city = db.Column(db.String(40), nullable=False, unique=False)
    country = db.Column(db.String(40), nullable=False, unique=False)
    hashed_password = db.Column(db.String(255), nullable=True)

    # posts = db.relationship('Post', backref='user', lazy=True)
    # comments = db.relationship('Comment', backref='user', lazy=True)
    # likes = db.relationship('Post', secondary=likedposts,
    #                         backref = db.backref('users', lazy='dynamic'),
    #                         lazy='dynamic')


    # @property
    # def password(self):
    #     return self.hashed_password

    # @password.setter
    # def password(self, password):
    #     self.hashed_password = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)
    def __init__(self, user_id, name, age, birthday, email, phone, city, country, hashed_password):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.city = city
        self.country = country
        self.hashed_password = hashed_password

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'age' : self.age,
    #         'birthday': self.birthday,
    #         'email': self.email,
    #         'city': self.city,
    #         'country': self.country,
    #         'hashed_password' : self.hashed_pasword
    #     }

    def json(self):
        return {"user_ID": self.user_id, "name": self.name, "age": self.age, "birthday": self.birthday,
                "email": self.email, "phone": self.phone, "city": self.city, "country": self.country, "hashed_password": self.hashed_password}

class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(40), nullable=False, unique=False)
    post_description = db.Column(db.String(40), nullable=True, unique=False)
    post_image = db.Column(db.String(255), nullable=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    

    # def to_dict(self):
    #     return {
    #         'post_id': self.post_id,
    #         'post_title': self.post_title,
    #         'post_description': self.post_description,
    #         'post_image': self.post_image,
    #         'user_id': self.user_id
    #     }

    def json(self):
        return {"post_id": self.post_id, "post_title": self.post_title, "post_description": self.post_description, "post_image": self.post_image,
                "user_id": self.user_id}


class LikedPost(db.Model):
    __tablename__ = 'liked_post'

    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'), primary_key=True ,nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), primary_key=True,nullable=False)

    def json(self):
        return {"post_id": self.post_id, "user_id": self.user_id}



class Comment(db.Model):
    __tablename__ = 'post_comment'

    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable = False)
    comment = db.Column(db.String(255), nullable=False, unique=False)

    # def to_dict(self):
    #     return {
    #         'comment_id': self.comment_id,
    #         'post_id': self.post_id,
    #         'user_id': self.user_id,
    #         'comment': self.comment
    #     }

    def json(self):
        return {"comment_id": self.comment_id, "post_id": self.post_id, "user_id": self.user_id, "comment": self.comment}
