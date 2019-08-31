# #if this page is executed with no errors, you have the "mysql.connector" module installed.
# import mysql.connector
# from GeneralVariable import userMysql, passwdMysql

# mydb = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='Elmariachi100@',
#     database='employees'
#      )
#
# print(mydb)
# mydb.close()

import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root',
                                  password='Elmariachi100@',
                                use_pure=False)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
