from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

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

    return render_template("profile/profile.html", user = username)    

