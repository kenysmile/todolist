from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import model as dbHandler
app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():

    items = dbHandler.selectUserID()
    error = None
    if request.method == 'POST':
        for (k,v) in items:
            if request.form['username'] == k and request.form['password'] == v:
                response = redirect(url_for("index"))
                response.set_cookie('user', k)
             #   response.set_cookie('id', a)
                return response
            else:
                error = 'Invalid.Please try again'
    return render_template('login.html', error = error)

@app.route('/index', methods=['GET', 'POST'])
def index():
    user_id = request.cookies.get('user')
    users = dbHandler.retrieveUsers(user_id)
    if request.method == 'POST':
        todo = request.form['work']
        ngay = request.form['date']

        dbHandler.insertUsersTodo(todo, ngay, users)
        dbHandler.retrieveUsers(user_id)

        response1 = redirect(url_for('add'))
        return response1

    return render_template('index.html', users = users, user_id = user_id)

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    user_id = request.cookies.get('user')
    users = dbHandler.retrieveUsers(user_id)
    if request.method == 'POST':
        todo = request.form['work']
        ngay = request.form['date']
        dbHandler.insertUsersTodo(todo, user_id, ngay)
        dbHandler.retrieveUsers(user_id)
        res = redirect(url_for('index'))
        res.set_cookie('todo', todo)
        return res
    else:
        error = None
    return render_template('index.html', users = users, error=error)

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     a = []
#     con = sqlite3.connect("pvt.db")
#     cur = con.cursor()
#     cur.execute("SELECT Use, pas FROM User")
#     items = cur.fetchall()
#     error = None
#
#     if request.method == 'POST':
#         name = request.form['user']
#         pas = request.form['pass']
#         dbHandler.registerUser(name, pas)
#         #print(dbHandler.registerUser(name, pas))
#         return redirect(url_for('login'))
#     return render_template('register.html', error=error)

    # if request.method == 'POST':
    #     name = request.form['user']
    #     pas = request.form['pass']
    #     for i, j in items:
    #         if i == name:
    #             error = 'No'
    #         else:
    #
    #             dbHandler.registerUser(name, pas)
    #             #print(dbHandler.registerUser(name, pas))
    #             return redirect(url_for('login'))
#     # return render_template('register.html', error=error)
# @app.route('/remove', ['GET', 'POST'])
# def remove():
#     a = []
#     user_id = request.cookies.get('user')
#     users = dbHandler.retrieveUsers(user_id)
#     if request.method == 'POST':
#         for user in users:
#             a.append(user)
#         dbHandler.removeUsers(user)
#         return redirect(url_for('index'))
#     return render_template('index.html')

# @app.route('/edit', methods=['GET', 'POST'])
# def edit():
#     user_id = request.cookies.get('user')
#
#     users = dbHandler.selectUserwhere(user_id)
#
#     if request.method == 'POST':
#         todoedit = request.form['todolist']
#         todo = dbHandler.retrieveUsers(user_id)
#         dbHandler.editUsers(todoedit, todo, user_id)
#         dbHandler.retrieveUsers(user_id)
#         return redirect(url_for('index'))
#
#     return render_template('edit.html', users = users, user_id = user_id)

if __name__ == '__main__':
    app.run(debug=True)
