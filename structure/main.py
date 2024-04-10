from flask import Blueprint, render_template, flash, redirect, url_for
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
    task = TaskForm()
    if task.validate_on_submit():
        new_task = Task(title=task.title.data, content=task.content.data, category=task.category.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully', 'success')
        return redirect(url_for('main.add_task'))
    return render_template('dashboard.html', form=task, user=current_user)

@main.route('/profile/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully', 'success')
    return redirect(url_for('main.add_task'))

@main.route('/profile/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_task(id):
    task = Task.query.filter_by(id=id).first()
    updated_data = TaskForm()
    if updated_data.validate_on_submit():
        task.title = updated_data.title.data
        task.content = updated_data.content.data
        task.category = updated_data.category.data
        db.session.commit()
        flash('Task updated successfully', 'success')
        return redirect(url_for('main.add_task'))
    return render_template('dashboard.html', form=updated_data, user=current_user)
