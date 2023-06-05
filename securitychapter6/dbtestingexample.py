import mysql.connector

connection = mysql.connector.connect(
  host="0.0.0.0",
  port=3306,
  user="root",
  password="mysecretpassword",
  database="DevnetDB"
)

cursor = connection.cursor()

# login de usuario y contrasena
username = input("Enter username: ")
password = input("Enter password: ")

# SQL query con string interpolation - MALA PRACTICA
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

cursor.execute(query)

result = cursor.fetchone()
print(result)
