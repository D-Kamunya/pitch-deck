from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch
from .forms import UpdateProfile,PitchForm
from .. import db,photos

# Views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    pitches=Pitch.get_all_pitches()
   
    return render_template('index.html',pitches=pitches)

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



@main.route('/profile/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.update_profile',username=username))    


@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = form.category.data
        # Updated review instance
        new_pitch = Pitch(pitch_title=title,pitch_body=body,pitch_category=category,user=current_user)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New Pitch Form'
    return render_template('new_pitch.html',title = title, pitch_form=form)    


@main.route('/pitches/category/<category_name>')
@login_required
def pitch_by_category(category_name):

    '''
    View root page function that returns pitch category page with pitches from category selected
    '''
    pitches=Pitch.query.filter_by(pitch_category=category_name).order_by(Pitch.posted.desc()).all()
    
    return render_template('pitch_by_category.html',pitches=pitches)



    