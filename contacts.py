import sqlite3

db = sqlite3.connect('contacts.sqlite')
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 2343432, 'stefunices@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1223, 'gsf@mail.ru')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("=" * 20)

cursor.close()
db.commit()
db.close()
