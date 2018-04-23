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
    username = session.get('username')
    erroradd = session.get('erroradd')
    todos = Show.query.filter(Show.name_id == Login.id).filter(Login.username == username)#show todo with username login
    return render_template('index.html', todos = todos[::-1], username = username, error1 = error1, erroradd = erroradd)

@app.route('/add', methods=['POST'])
def add():
    erroradd = None
    username = session.get('username') # username => user_id
    if request.method == 'POST':
        # name_id = db.session.query(Show.name_id).filter(Show.name_id == Login.id).filter(Login.username == username)
        name_id = db.session.query(Login.id).filter(Login.username == username)
        todo = Show(todo = request.form['todo'], ngay=request.form['ngay'], name_id = name_id)
        checkadd = Show.query.filter_by(todo = todo.todo, ngay = todo.ngay, name_id = todo.name_id).first()#check ID exited
        if checkadd:
            return redirect(url_for('index'))
        else:
            db.session.add(todo)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('index.html', erroradd = erroradd)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error2 = None
    if request.method == 'POST':
        new_user = request.form['a']
        new_password = request.form['b']
        new = Login(username=request.form['a'], password=request.form['b'])
        user = Login.query.filter_by(username=new_user).first()
        if user:
            error2 = 'Account already exists'
        else:
            new = Login(username=request.form['a'], password=request.form['b'])
            db.session.add(new)
            db.session.commit()      
            return redirect(url_for('acess'))
    return render_template('register.html', error2 = error2)      

@app.route('/acess', methods=['GET', 'POST'])
def acess():
    erroracess = None
    dblogin = Login.query.all()
    if request.method == 'POST':
        dblogin = Login.query.all()
        POST_USERNAME = request.form['username']
        POST_PASSWORD = request.form['password']
        user = Login.query.filter_by(username=POST_USERNAME, password=POST_PASSWORD).first()
        if user:
            session['username'] = POST_USERNAME
            return redirect(url_for('index'))
        else:
            erroracess = 'Incorrect password.!!!!!'
    return render_template('login.html', dblogin = dblogin, erroracess = erroracess)

@app.route('/search', methods = ['GET','POST'])
def search():
    errorsearch = None
    if request.method == 'POST':
        username = session.get('username')
        searchtodo = request.form['todo']
        a = Show.query.filter_by(todo=searchtodo).first()

        if a:
            todos = Show.query.filter(Show.name_id == Login.id).filter(Login.username == username).filter(Show.todo == searchtodo)
            return render_template('search.html', todos = todos, username = usename)      
        else:
            errorsearch = 'Data not found'
    return render_template('index.html', errorsearch = errorsearch)

@app.route('/delete/<id>')
def delete(id):
    logid = Show.query.get(id)
    db.session.delete(logid)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update', methods = ['POST'])
def update():
    if request.method == 'POST':
        show = Show.query.filter_by(id=request.form['id']).first()
        show.todo = request.form['todo']
        show.ngay = request.fotm['ngay']
        db.session.commit()
        return render_template('update.html')
        # return jsonify({'result':'sucess'})
    return render_template('index.html')
if __name__ == '__main__':

    app.run(debug = True)
