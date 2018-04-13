import sqlite3
import sys

cars = (
	('football', '2018-1-1','2'),
	('swimming', '2018-2-2', '3'),
	('walk', '2018-3-3', '1')
)


con = sqlite3.connect('test.db')

with con:
	cur = con.cursor()
    #
	# cur.execute("DROP TABLE IF EXISTS Todo")
	# cur.execute("CREATE TABLE Todo(ID INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT, ngay date, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES Login(ID))")

#	cur.executemany("INSERT INTO Todo(todo, ngay, user_id) VALUES(?, ?, ?)", cars)

    #
	# cur.execute("select user_id from Todo, Login where Todo.user_id = Login.ID and username = 'tu'", )
	# datas = cur.fetchall()
	# print(datas)


def selectUserID():
	con = sqlite3.connect("test.db")
	cur = con.cursor()
	cur.execute("select username, password from Login")
	datas = cur.fetchall()
	con.close()
	return datas

# a = selectUserID()
# for l, k, v in a:
# 	print(l)
# 	print(k)


def retrieveUsers(a):
	con = sqlite3.connect("test.db")
	cur = con.cursor()
	cur.execute("select todo, ngay from Todo, Login where Todo.user_id = Login.ID and username = ?", [a])
	users = cur.fetchall()
	con.close()
	return users

print(retrieveUsers('tu'))
# print(retrieveUsers('tu'))
def insertUsersTodo(todo, ngay, user_id):
	con = sqlite3.connect("test.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Todo(todo, ngay, user_id) VALUES (?, ?, ?)", (todo,  ngay, [user_id]))
	con.commit()
	con.close()

# pr#int(insertUsersTodo('game', '2018-4-5', user_id))


# print(insertUsersTodo(''))

# 	if y == 'tu' and z == 'phamvantu':
# 		print('Okie')
# 	else:
# 		print('false')
# def insertUser(username,password):
#     con = sqlite3.connect("tu.db")
#     cur = con.cursor()
#     cur.execute("INSERT INTO User(Use, Pas) VALUES(?,?)", (username,password))
#     con.commit()
#     con.close()
#
# def retrieveUsers(use):
# 	con = sqlite3.connect("tu.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT Todo FROM Todolist, User WHERE User.ID = Todolist.ID and Use = '%s' ORDER BY Ngay ASC " % use)
# 	users = cur.fetchall()
# 	con.close()
# 	return users
#
# def insertUsersTodo(todo, iduser, ngay):
# 	con = sqlite3.connect("tu.db")
# 	cur = con.cursor()
# 	cur.execute("INSERT INTO Todolist(Todo, ID, ngay) VALUES (?, ?, ?)", (todo, iduser, ngay))
# 	con.commit()
# 	con.close()
# #print(insertUsersTodo('game', '2018-2-2'))
# def retrieveUsersID(use):
# 	con = sqlite3.connect("tu.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT Todo FROM Todolist, User WHERE User.ID = Todolist.ID and Use = '%s' ORDER BY Ngay ASC " % use)
# 	users = cur.fetchall()
# 	con.close()
# 	return users

# print(retrieveUsersID('tu'))
#print(insertUsersTodo('walk', 2, '2018-8-8'))

# def registerUser(username,password):
#     con = sqlite3.connect("tu.db")
#     cur = con.cursor()
#     cur.execute("INSERT INTO Login (Use,pas) VALUES (?,?)", (username,password))
#     con.commit()
#     con.close()
# #print(registerUser('giang', 'nguyenxuangiang'), ('tu', 'phamvantu'), ('dong', 'caovangodng'), ('hau', 'nguyenhienhau'))
# def selectUser():
# 	con = sqlite3.connect('pvt.db')
# 	cur = con.cursor()
# 	cur.execute("select * from User")
# 	username = cur.fetchall()
# 	con.close()
#
# 	return username
#
# def selectUserwhere(use):
# 	con = sqlite3.connect('pvt.db')
# 	cur = con.cursor()
# 	cur.execute("select * from User where Use = '%s'" % use)
# 	username = cur.fetchall()
# 	con.close()
#
# 	return username
#
#
# def insertUsers(todo, use, ngay):
# 	con = sqlite3.connect("pvt.db")
# 	cur = con.cursor()
# 	cur.execute("INSERT INTO Phamtu (Todo, Use, ngay) VALUES (?, ?, ?)", (todo, use, ngay))
# 	con.commit()
# 	con.close()
# #print(insertUsers('Gym', 'Tu', '2018-8-8'))
#
# def retrieveUsers(name):
# 	con = sqlite3.connect("pvt.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT Todo FROM Phamtu WHERE Use = '%s' ORDER BY ngay ASC " % name)
# 	users = cur.fetchall()
# 	con.close()
# 	return users
#
# def editUsers(new, todo, use):
# 	con = sqlite3.connect('pvt.db')
# 	cur = con.cursor()
# 	cur.execute("update Phamtu set Todo = '%s' where Todo = '%s'" % (new, todo))
# 	con.commit()
# 	con.close()
#
# def removeUsers(todo):
# 	con = sqlite3.connect('pvt.db')
# 	cur = con.cursor()
# 	cur.execute("delete from Phamtu where Todo = '%s'" % todo)
# 	cur.fetchall()
# 	con.commit()
# 	con.close()

# print(retrieveUsers('Tu'))
# print(editUsers('bbb', 'aaa', 'Tu'))

#cur.execute("ALTER TABLE Phamtu ADD COLUMN ID INTEGER")












