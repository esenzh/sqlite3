import sqlite3

db = sqlite3.connect('contacts.sqlite')

update_sql = "UPDATE contacts SET email = 'update@mail.ru' WHERE contacts.phone = 6565"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close()