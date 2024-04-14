from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username is required."), Length(min=2, max=20, message="Username is too short.")], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(message="Email is required."), Email(message='Invalid email')], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(message="Password is required.")], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(message="Confirm Password is required."), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose a different one.')

    def validate_password(self, password):
        if len(password.data) < 8:
            raise ValidationError('Password should be at least 8 characters long')

    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != self.password.data:
            raise ValidationError('Passwords must match')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username is required.")], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired(message="Password is required.")], render_kw={"placeholder": "Password"})

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message="Title is required."), Length(min=2, max=15, message="Length should be between 2 and 15 characters.")], render_kw={"placeholder": "Title"})
    content = StringField('Content', validators=[DataRequired(message="Content is required."), Length(min=5)], render_kw={"placeholder": "Content"})
    category = RadioField('Category', validators=[DataRequired(message="Category is required.")], choices=[('1', 'Normal') ,('2', 'Urgent'), ('3', 'Important'), ('4', 'For later')])
