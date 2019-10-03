import sqlite3

db = sqlite3.connect('contacts.sqlite')

name = input('Please, enter the name: ')

for i in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
    print(i)



# for name, phone, email in db.execute("SELECT * FROM contacts"):
#     print(name)
#     print(phone)
#     print(email)

db.close()