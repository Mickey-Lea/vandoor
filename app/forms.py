from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QuestionsForm(FlaskForm):
    age = StringField('What is your age?', validators=[DataRequired()])
    gender = StringField('What is your gender?', validators=[DataRequired()])
    submit = SubmitField('Submit')