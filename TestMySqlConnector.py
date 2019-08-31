# #if this page is executed with no errors, you have the "mysql.connector" module installed.
import mysql.connector
from GeneralVariable import userMysql, passwdMysql
from mysql.connector import errorcode

# mydb = mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='Elmariachi100@',
#     database='employees'
#      )
#
# print(mydb)
# mydb.close()

# solving auth error
# https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported
# In MySQL 8.0, caching_sha2_password is the default authentication plugin rather than mysql_native_password
# and passing auth_plugin='mysql_native_password' did not work,
# because I accidentally installed mysql-connector instead of mysql-connector-python
try:
    cnx = mysql.connector.connect(
        user=userMysql,
        password=passwdMysql
        )
    print(cnx)
    cnx.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
