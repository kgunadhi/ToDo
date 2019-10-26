from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    taskTitle = StringField('Task Title', validators=[DataRequired()])
    taskTime = StringField('Time to complete task', validators=[DataRequired()])
    submit = SubmitField('Add')

class FinishedForm(FlaskForm):
    submit = SubmitField('Finished with top task')
