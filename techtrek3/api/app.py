from flask import Flask

from flask import (Flask, g, render_template, flash, redirect, url_for,abort)
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
							login_required, current_user)

import models
import forms

app = Flask(__name__)
app.debug = True
app.secret_key = ''
"""here secret_key is a random string of alphanumerics"""

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@app.before_request
def before_request():
	"""Connect to database before each request
		g is a global object, passed around all time in flask, used to setup things which
		we wanna have available everywhere.
	"""
    client = pymongo.MongoClient("")
    g.db = client['DBSDatabase']
	g.db.connect()
	g.user = current_user

@app.after_request
def after_request(response):
	"""close all database connection after each request"""
	g.db.close()
	return response


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}



@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    #Creates a new user and logs them in
	form = forms.SignUpForm()
	if form.validate_on_submit():
        user = models.User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
	return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@app.route('/login', methods = ('GET', 'POST'))
def login():
	form = forms.LoginForm()
	if form.validate_on_submit():
		user = models.User.query.filter(User.email == form.data['email']).first()
		login_user(user)
		return user.to_dict()
	return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return {'message': 'User logged out'}

@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401


@app.route('/new_post', methods = 'POST')
@login_required
def post():
	form = forms.PostForm()
	if form.validate_on_submit():

        post = models.Post(
        post_title=form.data['Post Title'],
        post_description=form.content.data.strip() #form.data['Post Desc']
        )
        db.session.add(post)
        db.session.commit()

        post_dict = post.to_dict()


        post = models.LikedPost(
            user_id=g.user.id,
            post_id= post_dict['post_id']
        )
        db.session.add(post)
        db.session.commit()

		return post_dict



if __name__ == '__main__':
    app.run(debug=True)
