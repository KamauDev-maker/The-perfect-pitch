from wtforms.validators import InputRequired
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm

class PitchForm(FlaskForm):
    
    content = TextAreaField('INPUT YOUR PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    
    opinion = TextAreaField('WRITE A COMMENT')
    submit = SubmitField('SUBMIT')

class CategoryForm(FlaskForm):
    
    name =  StringField('Category Name', validators=[InputRequired()])
    submit = SubmitField('Create')
