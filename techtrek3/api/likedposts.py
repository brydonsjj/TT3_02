likedposts = db.Table('likedposts',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'), primary_key=True),
    db.Column('post_is', db.Integer, db.ForeignKey('posts.post_id'), primary_key=True)
)