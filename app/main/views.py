from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .forms import UpdateProfile
from .. import db
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

@main.route('/profile/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',user=user,form =form)