from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(60), nullable=False)
    team = db.Column(db.String(60), nullable=False)
    name =  db.Column(db.String(60), nullable=False)