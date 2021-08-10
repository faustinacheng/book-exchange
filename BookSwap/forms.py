from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from BookSwap.models import User


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


class RegisterForm(FlaskForm):
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address.')

    def validate_username(self, username_to_check):
        username = User.query.filter_by(username=username_to_check.data).first()
        if username:
            raise ValidationError('Username already exists! Please try a different username.')

    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    username = StringField(label='Username:', validators=[
        Length(min=4, max=30, message='Username must be between 4 to 30 characters long.'), DataRequired()])
    email_address = StringField(label='Email Address:',
                                validators=[Email(message='Email address is invalid.'), DataRequired()])
    password1 = PasswordField(label='Password:',
                              validators=[Length(min=6, message='Password must be at least 6 characters long.'),
                                          DataRequired()])
    password2 = PasswordField(label='Confirm Password:',
                              validators=[EqualTo(fieldname='password1', message='Passwords do not match.'),
                                          DataRequired()])
    submit = SubmitField(label='Sign Up')


class AddBooksSearch(FlaskForm):
    title = StringField(label='Title:')
    author = StringField(label='Author:')
    submit = SubmitField(label='Search')


class AddBooksForm(FlaskForm):
    submit = SubmitField(label='Add')
