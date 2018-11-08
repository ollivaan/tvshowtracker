from application import db

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    episodes_total = db.Column(db.Integer, nullable=False)

    def __init__(self, name):
        self.name = name
        self.episodes_total = 0;