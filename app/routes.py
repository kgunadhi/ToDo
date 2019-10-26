from flask import render_template, flash, redirect
from app import app, db
from app.forms import TaskForm, FinishedForm
from app.models import Task

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form1 = TaskForm()
    if form1.validate_on_submit():
        task = Task(title=form1.taskTitle.data, minutes=form1.taskTime.data)
        db.session.add(task)
        db.session.commit()
        return redirect('/index')
    form2 = FinishedForm()
    if form2.validate_on_submit():
        first = Task.query.first()
        if first:
            db.session.delete(first)
        db.session.commit()
        return redirect('/index')
    taskList = Task.query.all()
    return render_template('index.html', title='Home', taskList=taskList, form1=form1, form2=form2)
