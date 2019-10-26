from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
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
    return render_template('index.html', title='Home', task=taskExample, taskList=taskList)
