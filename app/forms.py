from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    taskTitle = StringField('Task name', validators=[DataRequired()])
    taskTime = StringField('Minutes to complete task', validators=[DataRequired()])
    submit = SubmitField('Add')

class FinishedForm(FlaskForm):
    taskFinished = BooleanField('Completed first task?', validators=[DataRequired()])
    submit = SubmitField('Yay!')
