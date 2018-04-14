from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tupham/PycharmProjects/phamvantu/data.db'
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
db.create_all()
api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(show, methods=['GET', 'POST', 'PUT', 'DELETE'])

@app.route('/index')
def index():
    return 'Hello World!'



@app.route('/login')
def login():     
    POST_USERNAME = request.form['username']
    POST_PASSWORD = request.form['password']
                
    user = login.query.filter_by(username=POST_USERNAME, password=POST_PASSWORD).first()
    if user:
        return redirect(url_for('index'))
    else:
        return render_template('login.html')
    # return 'yes'

if __name__ == '__main__':
    app.run(debug = True)
