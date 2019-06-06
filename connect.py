import mysql.connector

db_connect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'abit850923',
    database = '',
)

cursor = db_connect.cursor()


