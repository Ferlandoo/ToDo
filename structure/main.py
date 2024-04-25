from flask import Blueprint, render_template, flash, redirect, url_for, jsonify, request
from flask_login import login_required, current_user
from sqlalchemy import or_, and_
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
    else:
        for field, errors in task.errors.items():
            for error in errors:
                flash(''.join(error), 'error')
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

@main.route('/profile/search', methods=['GET', 'POST'])
@login_required
def search_task():
    search_task = request.form.get('search')
    if search_task == "" or search_task == None:
        return redirect(url_for('main.no_results'))
    else:
        task = TaskForm()
        tasks_searched = Task.query.filter(and_(
            Task.user_id == current_user.id, or_(
                Task.title.contains(search_task), 
                Task.content.contains(search_task)
                ))).all()
        if tasks_searched == []:
            return redirect(url_for('main.no_results'))
    return render_template('search.html', search=tasks_searched, actual = search_task, form=task)

@main.route('/profile/filter', methods=['GET', 'POST'])
@login_required
def filter_task():
    category = request.form.get('category')
    category_number ={'normal': 1, 'urgent': 2, 'important': 3, 'for-later': 4}
    if category is None:
        return redirect(url_for('main.add_task'))
    else:
        task = TaskForm()
        if category == 'all':
            tasks_filtered = Task.query.filter_by(user_id=current_user.id).all()
        else:
            tasks_filtered = Task.query.filter(Task.category==category_number[category], Task.user_id==current_user.id).all()
    return render_template('filter.html', filter=tasks_filtered, user=current_user, form=task)

@main.route('/profile/no_results')
@login_required
def no_results():
    return render_template('no_results.html')
