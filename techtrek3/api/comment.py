import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Comment(db.Model, UserMixin):
    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), nullable = False)
    comment = db.Column(db.String(255), nullable=False, unique=False)

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'comment': self.comment
        }