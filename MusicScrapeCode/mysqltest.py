# from msilib.schema import tables
from sqlite3 import Cursor
# from venv import create
import pymysql
# import mysql.connector


endpoint = 'mysql-bandscrape.cpzuexvbklch.us-east-1.rds.amazonaws.com'
username = 'admin'
password = 'nayrryan123'
database_name = 'test'

connection = pymysql.connect(host=endpoint, user=username, password=password, database=database_name)
cursor = connection.cursor()

mac = ("cat")
mohan = ("dog")
june = ("cow")


# SQLvalues = (mac, mohan, listtest1)

cursor.execute("""INSERT INTO BandInfo(Artist, Date, Time)
VALUES (%s, %s, %s)""", (mac, mohan, june)) 

cursor.execute('select * from BandInfo')
output = cursor.fetchall()
for i in output:
    print(i)


# # connection.commit()

# cursor.execute('select * from BandInfo')
# output = cursor.fetchall()
# for i in output:
#     print(i)



# print (dbs)

    # rows = cursor.fetchall()

    # for row in rows:
    #     print ("{0} {1} {2}".format(row[0], row[1], row[2]))
# print (Cursor)
# handler()

