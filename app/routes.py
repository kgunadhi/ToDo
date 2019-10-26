from flask import render_template, flash, redirect
from app import app
from app.forms import TaskForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    taskExample = {'Title': 'Watch webcast', 'Time': '45'}
    taskList = [
        {
            'Title': 'Bio Reading',
            'Time': '15'
        },
        {
            'Title': 'Problem Set',
            'Time': '20'
        }
    ]

    taskListSoft = []
    form = TaskForm()
    if form.validate_on_submit():
        flash('Task to complete: {}, in {} minutes'.format(
            form.taskTitle.data, form.taskTime.data))
        taskListSoft.append({'Title': form.taskTitle.data, 'Time': form.taskTime.data})
        return redirect('/index')
    return render_template('index.html', title='Home', task=taskExample, taskList=taskListSoft, form=form)
