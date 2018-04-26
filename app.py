from flask import Flask, render_template, request, redirect, url_for, json, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/tupham/PycharmProjects/phamvantu/data.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'super secret'    

api = Api(app)

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

class TodoRes(Resource):
    def post(self):

        json = request.get_json()
        id = json['id']
        todo = json['todo']
        ngay = json['ngay']
        checkupdate = Show.query.filter_by(todo = todo, ngay = ngay).first() # check data update
        
        if checkupdate:
            return redirect(url_for('index'))
        else:
            Show.query.filter_by(id=id).update(dict(todo=json['todo'], ngay=json['ngay']))
            db.session.commit()
            return {"sucess": 1}

api.add_resource(TodoRes, '/api/todo')

@app.route('/')
def home():
    return redirect(url_for('acess'))

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
        name_id = db.session.query(Login.id).filter(Login.username == username) #show id with
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
        user = Login.query.filter_by(username=new_user).first() # check user
    
        if user: # check user exited
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
        user = Login.query.filter_by(username=POST_USERNAME, password=POST_PASSWORD).first() # check user, pass Login
    
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
        searchdata = Show.query.filter_by(todo = searchtodo).first() # check search data

        if searchdata:
            todos = Show.query.filter(Show.name_id == Login.id).filter(Login.username == username).filter(Show.todo == searchtodo)
            return render_template('search.html', todos = todos)      
        else:
            errorsearch = 'Data not found'
    
    return render_template('index.html', errorsearch = errorsearch, username = username)

@app.route('/delete/<id>')
def delete(id):
    logid = Show.query.get(id)
    db.session.delete(logid)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
