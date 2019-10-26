from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    minutes = db.Column(db.String(120), index=True, unique=True)
    start = db.Column(db.String(120), index=True, unique=True)
    end = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Task {} for {} minutes>'.format(self.title, self.minutes)
