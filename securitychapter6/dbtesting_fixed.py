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

# SQL query usando parametros - SQL injection SAFE
query = "SELECT * FROM users WHERE username=%s AND password=%s"
params = (username, password)

cursor.execute(query, params)

result = cursor.fetchone()
print(result)