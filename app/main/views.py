from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
# Views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    return render_template('index.html')

@main.route('/profile/<username>')
def profile(username):

    '''
    View profile page function that returns the profile details of the current user logged in
    '''
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    

