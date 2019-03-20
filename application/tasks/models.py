from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    tekoaika = db.Column(db.Integer)
    vaikeusarvio = db.Column(db.String(10)

    def __init__(self, name):
        self.name = name
        self.done = False
