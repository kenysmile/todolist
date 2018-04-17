from flask import Flask, render_template, request, redirect, url_for, json, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tupham/PycharmProjects/phamvantu/data.db'
#SQLALCHEMY_TRACK_MODIFICATION = True
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'super secret'    


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    def __init__(self, username, password):
        self.username = username
        self.password = password
class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50))
    ngay = db.Column(db.String(50))
    name_id = db.Column(db.Integer, db.ForeignKey('login.id'))
    _name = db.relationship('Login')
    def __init__(self, todo, ngay, name_id):
        self.todo = todo
        self.ngay = ngay
        self.name_id = name_id
db.create_all()
# api_manager = APIManager(app, flask_sqlalchemy_db=db)
# api_manager.create_api(show, methods=['GET', 'POST', 'PUT', 'DELETE'])

@app.route('/index')
def index():
    error1 = None
    a = Show.query.all()
    b = Login.query.all()
    # searchtodo = request.form['todo']


    username = session.get('username')
    todos = Show.query.filter(Show.name_id == Login.id).filter(Login.username == username)
    return render_template('index.html', todos = todos, username = username, error1 = error1)

@app.route('/add', methods=['POST'])
def add():
    a = Show.query.all()
    b = Login.query.all()
    username = session.get('username')
    if request.method == 'POST':
        name_id = db.session.query(Show.name_id).filter(Show.name_id == Login.id).filter(Login.username == username)
        todo = Show(todo = request.form['todo'], ngay=request.form['ngay'], name_id = name_id)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    error2 = None
    if request.method == 'POST':
        new = Login(username=request.form['a'], password=request.form['b'])
        if new:
            error2 = 'Account already exists.'
        else:

            db.session.add(new)
            db.session.commit()
        # session['new'] = new
        # return render_template('login.html')
            return redirect(url_for('acess'))
    return render_template('register.html', error2 = error2)

@app.route('/acess', methods=['GET', 'POST'])
def acess():
    dblogin = Login.query.all()

    if request.method == 'POST':
        dblogin = Login.query.all()
        POST_USERNAME = request.form['username']
        POST_PASSWORD = request.form['password']

        user = Login.query.filter_by(username=POST_USERNAME, password=POST_PASSWORD).first()
        if user:
            session['username'] = POST_USERNAME
            return redirect(url_for('index'))
    return render_template('login.html', dblogin = dblogin)

@app.route('/delete/<id>')
def delete(id):
    logid = Show.query.get(id)
    db.session.delete(logid)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/search', methods = ['GET','POST'])
def search():
    error = None
    if request.method == 'POST':
        username = session.get('username')
        searchtodo = request.form['todo']
        todos = Show.query.filter(Show.name_id == Login.id).filter(Login.username == username).filter(Show.todo == searchtodo)        
        return render_template('search.html', todos = todos, username = username)
    else:
        error = 'You can not found'
    return render_template('index.html', error = error)
# @app.route('/update/<id>')
# def update(id):

#     if request.method == 'POST':
#         return 'OKie'
#     return render_template('update.html')
if __name__ == '__main__':

    app.run(debug = True)
