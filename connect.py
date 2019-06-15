import mysql.connector

db_connect = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'abit850923',
    database = '',
)

cursor = db_connect.cursor()

cursor.execute('SELECT * FROM project.company')
result = cursor.fetchall()
print(result)

company_ID = []
company_name = []


for rows in result:
    adjust = list(rows)
    company_ID.append(adjust[0])
    company_name.append(adjust[1])
print(company_ID)
print(company_name)
