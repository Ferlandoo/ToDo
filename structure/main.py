from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from .forms import TaskForm
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully', 'success')
    return render_template('dashboard.html', form=form, user=current_user)
