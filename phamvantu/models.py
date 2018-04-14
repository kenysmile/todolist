from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tupham/PycharmProjects/phamvantu/test.db'
#SQLALCHEMY_TRACK_MODIFICATION = True
db = SQLAlchemy(app)

class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    def __init__(self, username, password):
        self.username = username
        self.password = password
class show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50))
    ngay = db.Column(db.String(50))
    def __init__(self, todo, ngay):
        self.todo = todo
        self.ngay = ngay