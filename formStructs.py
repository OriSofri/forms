from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, equal_to 

class RegistrationForm (FlaskForm): 
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(),
                                                 equal_to('password')])
    submit = SubmitField('sign-up')

class LoginForm (FlaskForm): 
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('sign-in')
