import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

new_username = "CodingPro"
new_email = "pro@example.com"


cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (new_username, new_email))

connection.commit()

connection.close()

print("Data added successfully!")