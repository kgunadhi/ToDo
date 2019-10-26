from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    taskTitle = StringField('Task Title', validators=[DataRequired()])
    taskTime = StringField('Time to complete task', validators=[DataRequired()])
    submit = SubmitField('Add')
