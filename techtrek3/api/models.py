from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/socialmedia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True,)
    name = db.Column(db.String(40), nullable=False, unique=True)
    age = db.Column(db.DateTime, nullable=False, unique=False)
    birthday = db.Column(db.String(40), nullable=False, unique=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    city = db.Column(db.String(40), nullable=False, unique=False)
    country = db.Column(db.String(40), nullable=False, unique=False)
    hashed_password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    posts = db.relationship('Post', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    likes = db.relationship('Post', secondary=likedposts,
                            backref = db.backref('users', lazy='dynamic'),
                            lazy='dynamic')


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age' : self.age,
            'birthday': self.birthday,
            'email': self.email,
            'city': self.city,
            'country': self.country,
            'hashed_password' : self.hashed_pasword,
            'is_admin': self.is_admin,
        }

    def json(self):
        return {"user_ID": self.user_ID, "name": self.name, "age": self.age, "birthday": self.birthday,
                "email": self.email, "phone": self.phone, "city": self.city, "country": self.city}

class Post(db.Model, UserMixin):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(40), nullable=False, unique=False)
    post_description = db.Column(db.String(40), nullable=True, unique=False)
    post_image = db.Column(db.String(255), nullable=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'post_title': self.post_title,
            'post_description': self.post_description,
            'post_image': self.post_image,
            'user_id': self.user_id,
            'comments': self.comments
        }


class LikedPost(db.Model):
    __tablename__ = 'liked_post'

    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'), primary_key=True ,nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), primary_key=True,nullable=False)



class Comment(db.Model, UserMixin):
    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable = False)
    comment = db.Column(db.String(255), nullable=False, unique=False)

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'comment': self.comment
        }
