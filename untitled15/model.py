import sqlite3
a = []
b = []
# tu = (
# 	('tu', 'phamvantu'),
# 	('tuan', 'nguyentrongtuan'),
# 	('nam', 'giangvannam')
# )
con = sqlite3.connect('pvt.db')
cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS Login")
# cur.execute("CREATE TABLE Login(Use TEXT PRIMARY KEY , pas TEXT)")
# cur.executemany("INSERT INTO Login(Use, pas) VALUES(?, ?)", tu)
#

def registerUser(username,password):
    con = sqlite3.connect("pvt.db")
    cur = con.cursor()
    cur.execute("INSERT INTO User (Use,pas) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def selectUser():
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("select * from User")
	username = cur.fetchall()
	con.close()

	return username

def selectUserwhere(use):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("select * from User where Use = '%s'" % use)
	username = cur.fetchall()
	con.close()

	return username


def insertUsers(todo, use, ngay):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Phamtu (Todo, Use, ngay) VALUES (?, ?, ?)", (todo, use, ngay))
	con.commit()
	con.close()
#print(insertUsers('Gym', 'Tu', '2018-8-8'))

def retrieveUsers(name):
	con = sqlite3.connect("pvt.db")
	cur = con.cursor()
	cur.execute("SELECT Todo FROM Phamtu WHERE Use = '%s' ORDER BY ngay ASC " % name)
	users = cur.fetchall()
	con.close()
	return users

def editUsers(new, todo, use):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("update Phamtu set Todo = '%s' where Todo = '%s'" % (new, todo))
	con.commit()
	con.close()

def removeUsers(todo):
	con = sqlite3.connect('pvt.db')
	cur = con.cursor()
	cur.execute("delete from Phamtu where Todo = '%s'" % todo)
	cur.fetchall()
	con.commit()
	con.close()

# print(retrieveUsers('Tu'))
# print(editUsers('bbb', 'aaa', 'Tu'))





