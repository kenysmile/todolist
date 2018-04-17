import sqlite3
a = 'Tuan'
import model as dbHandler
b = 'nguyentrongtuan'
con = sqlite3.connect("pvt.db")
# cur = con.cursor()
# cur.execute("SELECT Use, pas FROM User")
# items = cur.fetchall()

todoedit = "ddd"
todo = dbHandler.retrieveUsers('Tu')
user_id = 'Tu'
dbHandler.editUsers(todoedit, todo, user_id)
data = dbHandler.retrieveUsers(user_id)
print(data)

print(todo)
