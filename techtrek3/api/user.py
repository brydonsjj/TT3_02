import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(40), nullable=False, unique=True,)
    name = db.Column(db.String(40), nullable=False, unique=True)
    age = db.Column(db.DateTime, nullable=False, unique=False)
    birthday = db.Column(db.String(40), nullable=False, unique=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    city = db.Column(db.String(40), nullable=False, unique=False)
    country = db.Column(db.String(40), nullable=False, unique=False)
    hashed_password = db.Column(db.String(255), nullable=False)
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
            'hashed_password' = self.hashed_pasword,
            'posts' = self.posts,
            'comments' = self.comments,
            'likes' = self.likes
        }

