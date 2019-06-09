import mysql.connector

db_connect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'dbstudent',
    password = 'dbstudent',
    database = 'project',
    auth_plugin='mysql_native_password'
)

cursor = db_connect.cursor()


