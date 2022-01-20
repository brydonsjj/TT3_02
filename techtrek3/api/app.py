from flask import Flask

from flask import (Flask, g, render_template, flash, redirect, url_for,abort)
from flask_bcrypt import check_password_hash
from flask_login import (LoginManager, login_user, logout_user,
							login_required, current_user)

from user import User
from signup_form import SignUpForm
from login_form import LoginForm

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
	form = SignUpForm()
	if form.validate_on_submit():
        user = User(
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
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter(User.email == form.data['email']).first()
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





if __name__ == '__main__':
    app.run(debug=True)