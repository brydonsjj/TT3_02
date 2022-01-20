import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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