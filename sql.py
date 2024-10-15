import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

cursor = connection.cursor()
