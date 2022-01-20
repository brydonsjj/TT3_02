from flask import Flask, jsonify
from flask_login import (login_user, logout_user,
                     login_required)
import models
import forms
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/socialmedia'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

db = SQLAlchemy(app)
CORS(app)

# @auth_routes.route('/signup', methods=['POST'])
# def sign_up():
#     #Creates a new user and logs them in
# 	form = forms.SignUpForm()
# 	if form.validate_on_submit():
#         user = models.User(
#             username=form.data['username'],
#             email=form.data['email'],
#             password=form.data['password']
#         )
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         return user.to_dict()
# 	return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@app.route('/login', methods = ['GET'])
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		user = models.User.query.filter(models.User.email == form.data['email']).first()
		login_user(user)
		return user.to_dict()
	return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return {'message': 'User logged out'}



@app.route('/new_post', methods = ['POST'])
@login_required
def post():
    form = forms.PostForm()
    if form.validate_on_submit():

        post = models.Post(
        post_title=form.data['Post Title'],
        post_description=form.data['Post Desc'],
        post_image = form.data['post_image'],
        user_id= form.data['user_id']
        )

    try: 
        db.session.add(post)
        db.session.commit()
    except: 
        return False

    return True

@app.route('/posts', methods=['GET'])
@login_required
def get_all_posts(): 
    return jsonify({"posts": [models.Post.json() for post in models.Post.query.all()]})

@app.route('/posts/<string:user_id>', methods=['GET'])
@login_required
def get_user_posts(user_id): 
    return jsonify({"user posts": [models.Post.json() for post in models.Post.query.filter_by(user_id=models.User.user_id)]})

@app.route('/posts/update/<string:post_id>', methods=['POST'])
@login_required
def update_post(post_id):
    post = models.Post.query.filter_by(post_id=post_id).first()
    if post:
        data = request.get_json()
        models.Post.post_id = data["post_id"]
        models.Post.post_title = data["post_title"]
        models.Post.post_description = data["post_description"]
        models.Post.post_image = data["post_image"]
        models.Post.user_id = data["user_id"]
    try:
        db.session.commit()
    except:
        return jsonify({"message": "Error updating post"}), 500
    return jsonify(post.json(), 201)

@app.route('/posts/update/<string:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = models.Post.query.filter_by(post_id=post_id).first()
    if post:
        try:
            db.session.delete(post)
            db.session.commit()
        except:
            return jsonify({"message": "Error deleting post"}), 500
    return 201


@app.route('/', methods=['GET'])
def get_all_users():
    return jsonify({"users": [models.User.json() for user in models.User.query.all()]})


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5010, debug=True)
