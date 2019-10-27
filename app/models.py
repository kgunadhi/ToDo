from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=False)
    minutes = db.Column(db.String(120), index=True, unique=False)
    start = db.Column(db.String(120), index=True, unique=False)
    end = db.Column(db.String(120), index=True, unique=False)

    def __repr__(self):
        return '<Task {} for {} minutes>'.format(self.title, self.minutes)
