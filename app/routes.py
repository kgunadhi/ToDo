from flask import render_template, flash, redirect
from app import app, db
from app.forms import TaskForm
from app.models import Task

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.taskTitle.data, minutes=form.taskTime.data)
        db.session.add(task)
        db.session.commit()
        return redirect('/index')
    taskList = Task.query.all()
    return render_template('index.html', title='Home', taskList=taskList, form=form)
