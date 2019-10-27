from flask import render_template, flash, redirect
from app import app, db
from app.forms import TaskForm, FinishedForm
from app.models import Task
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form1 = TaskForm()
    if form1.validate_on_submit():
        if Task.query.first() is None:
            time = str(datetime.now().time())
            time = time.split(':')[0] + ":" + time.split(':')[1]
        else:
            time = Task.query.order_by(Task.start.desc()).first().end
        endTime = addMinutes(time, int(form1.taskTime.data))
        task = Task(title=form1.taskTitle.data, minutes=form1.taskTime.data, start=time, end=endTime)
        db.session.add(task)
        db.session.commit()
        return redirect('/index')
    form2 = FinishedForm()
    if form2.validate_on_submit():
        if form2.taskFinished.data == True:
            first = Task.query.first()
            if first:
                db.session.delete(first)
                db.session.commit()
                time = str(datetime.now().time())
                prevEnd = time.split(':')[0] + ":" + time.split(':')[1]
                for t in Task.query.all():
                    start = prevEnd
                    end = addMinutes(start, t.minutes)
                    prevEnd = end
                    task = Task(title=t.title, minutes=t.minutes, start=start, end=end)
                    db.session.add(task)
                    db.session.delete(t)
                    db.session.commit()
        return redirect('/index')
    taskList = Task.query.all()
    return render_template('index.html', title='Home', taskList=taskList, form1=form1, form2=form2)

def addMinutes(time, minutes):
    hour = int(time.split(':')[0]) + int(minutes) // 60
    min = int(time.split(':')[1]) + int(minutes) % 60
    if min >= 60:
        hour += 1
        min -= 60
    if min < 10:
        min = "0" + str(min)
    return str(hour) + ":" + str(min)
