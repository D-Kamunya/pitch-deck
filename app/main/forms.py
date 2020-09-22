from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Edit your bio',validators = [Required()])
    submit = SubmitField('Edit bio')


class PitchForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    body = TextAreaField('Movie review')
    category = SelectField(u'Category', choices=[('Investors', 'Investors'), 
                                                ('Customers', 'Customers'),
                                                ('Sales', 'Sales'),
                                                ('Employess', 'Employess'),
                                                ('Partners', 'Partners'),
                                                ('Competitors', 'Competitors'),
                                                ('Other', 'Other') ])
    submit = SubmitField('PITCH')
