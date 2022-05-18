from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[InputRequired()])
    blog = TextAreaField('Write Blog...')
    submit = SubmitField('submit')
    
class CommentForm(FlaskForm):
    title = StringField('Comment Title', validators=[InputRequired()])
    comment = TextAreaField('Comments...')
    submit = SubmitField('submit')
    
class BioForm(FlaskForm):
    bio = TextAreaField('Write A Short Bio About You...')
    submit = SubmitField('Submit')