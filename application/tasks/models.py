from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    tekoaika = db.Column(db.Integer)
    vaikeusarvio = db.Column(db.String(144))
    name = db.Column(db.String(144))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, tekoaika, vaikeusarvio, account_id):
        self.tekoaika = tekoaika
        self.vaikeusarvio = vaikeusarvio
        self.name = name
        self.account_id = account_id