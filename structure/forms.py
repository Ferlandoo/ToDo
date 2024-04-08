from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            flash('That username is taken. Please choose a different one.', 'error')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('That email is taken. Please choose a different one.', 'error')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Title"})
    content = StringField('Content', validators=[DataRequired(), Length(min=5)], render_kw={"placeholder": "Content"})
