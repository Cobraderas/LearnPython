# #if this page is executed with no errors, you have the "mysql.connector" module installed.
import mysql.connector
# from GeneralVariable import userMysql, passwdMysql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Elmariachi100@"
)

print(mydb)
