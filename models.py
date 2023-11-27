from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(48), unique=True)

    def __repr__(self):
        return f'Бот: {self.mac[:12]}'



db.create_all()
