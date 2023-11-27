from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DATABASE_URL

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

try:
    from controller import *
except:
    pass

if __name__ == '__main__':
    from controller import *

    app.run()
