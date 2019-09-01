import mysql.connector  # if this is executed with no errors, you have the "mysql.connector" module installed.
from GeneralVariable import userMysql, passwdMysql  # imports some general variables stored outside project
# from mysql.connector import errorcode


# solving auth error
# https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported
# In MySQL 8.0, caching_sha2_password is the default authentication plugin rather than mysql_native_password
# and passing auth_plugin='mysql_native_password' did not work,
# because I accidentally installed mysql-connector instead of mysql-connector-python
# try:
#     cnx = mysql.connector.connect(
#         host='localhost',
#         user=userMysql,
#         password=passwdMysql
#         )
#     print(cnx)
#     cnx.close()
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#     cnx.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql
# )
#
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mytestdb")  # creates the db mytestdb
# mycursor.execute("SHOW DATABASES")  # check if database exists
# for x in mycursor:
#     print(x)
#
# mydb.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# connect to previously created mytestdb database
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
#
# # creates table and sets 2 columns name and address to type varchar at 255
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mydb.close()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Return a list of your system's databases
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
#
# # if a table exist by listing all tables in your database with the "SHOW TABLES" statement
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#     print(x)
#
# mydb.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# defining a PRIMARY KEY
# use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1,
# and increased by one for each record
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
#
# mycursor = mydb.cursor()
# # commented out the line below since the table existed already otherwise is good to use it from creation as below
# mycursor.execute("CREATE TABLE customers /"
#                  " (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#
#
# # If the table already exists, use the ALTER TABLE keyword
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mydb.close()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# To fill a table in MySQL, use the "INSERT INTO" statement
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Farfuridi", "Pipera 99")  # insert only 2 values
#
# mycursor.execute(sql, val)
# mydb.commit()  # is required to make the changes, otherwise no changes are made to the table
#
# print(mycursor.rowcount, "record inserted")
# mydb.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# to Insert Multiple Rows use the executemany() method
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('Marcel', 'Strada Plopului nr 10'),
#     ('Vasile', 'Bld Plopului nr 11'),
#     ('Iliuta', 'Strada Lui nr 12'),
#     ('Gogu', 'Bld Plopu nr 113'),
#     ('Dan', 'Aleea Opu nr 122'),
#     ('Cizmel', 'Strada Mopului nr 20'),
#     ('Anton', 'Intrarea Flopului nr 40'),
#     ('Beton', 'Strada Dopului nr 410'),
#     ('Cocalici', 'Str Panalopului nr 102'),
#     ('Mamalig', 'Fundatura Sopului nr 1'),
#     ('Viorica', 'Bld Zopului nr 18'),
#     ('Leana', 'Strada Mortului nr 19'),
#     ('Gigica', 'Aleea Clopului nr 120')
# ]
#
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted")
#
# mydb.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Get Inserted ID
# get the id of the row you just inserted by asking the cursor object
# If you insert more that one row, the id of the last inserted row is returned
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Matrangel", " Bld I.C. Bratianu nr. 55")
#
# mycursor.execute(sql, val)
# mydb.commit()
#
# print("1 record inserted, ID: ", mycursor.lastrowid)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# select from table use SELECT statement
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM customers")  # select all
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
#
# print(" ")
#
# # select only some of the columns in a table, use the "SELECT" statement followed by the column name(s)
# mycursor.execute("SELECT name, address FROM customers")
#
# myresult = mycursor.fetchall()  # use the fetchall() method, which fetches all rows from the last executed statement
#
# for x in myresult:
#     print(x)
#
# print(" ")
#
# # fetchone() method will return the first row of the result
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)
#
# mydb.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# selecting records from a table, you can filter the selection by using the "WHERE" statement
mydb = mysql.connector.connect(
    host='localhost',
    user=userMysql,
    password=passwdMysql,
    database='mytestdb'
)

mycursor = mydb.cursor()

# Select record(s) where the address is "Bld Zopului nr 18": result
sql = "SELECT * FROM customers WHERE address = 'Bld Zopului nr 18'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print(' ')

# using wildcards when selecting the records that starts, includes, or ends with a given letter or phrase.
sql = "SELECT * FROM customers WHERE address LIKE '%Bld%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print(' ')

# Preventing SQL injections
# When query values are provided by the user, you should escape the values
# mysql.connector module has methods to escape query values
# Escape query values by using the placholder %s method
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Fundatura Sopului nr 1", )

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

print(' ')

# sorting the results with ORDER BY and ASC or DESC
# sql = "SELECT * FROM customers ORDER BY name ASC"  # sorting the results with ORDER BY and ASC
sql = "SELECT * FROM customers ORDER BY name DESC"   # sorting the results with ORDER BY and DESC
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print(' ')

mydb.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# delete records from an existing table by using the "DELETE FROM" statement
mydb = mysql.connector.connect(
    host='localhost',
    user=userMysql,
    password=passwdMysql,
    database='mytestdb'
)

mycursor = mydb.cursor()

# update existing records in a table by using the "UPDATE" statement
# WHERE clause specifies which record or records that should be updated.
# If you omit the WHERE clause, all records will be updated!
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Aleea Opu nr 122'"


# WHERE clause specifies which record(s) that should be deleted.
# If you omit the WHERE clause, all records will be deleted!
# sql = "DELETE FROM customers WHERE id = '2'"

# sql = "DROP TABLE customers"  # deletes the entire table
# mycursor.execute(sql)  # only this statement is necessary for the drop table to execute

# sql = "DROP TABLE IF EXISTS customers"  # drops table only if exists
# mycursor.execute(sql)

mycursor.execute(sql)
mydb.commit()  # mydb.commit(). It is required to make the changes, otherwise no changes are made to the table
# print(mycursor.rowcount, "record(s) deleted")
print(mycursor.rowcount, "record(s) affected")  # executed when update is performed

mydb.close()

print(' ')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

mydb = mysql.connector.connect(
    host='localhost',
    user=userMysql,
    password=passwdMysql,
    database='mytestdb'
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

mydb.close()

print(' ')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# You can limit the number of records returned from the query, by using the "LIMIT" statement
mydb = mysql.connector.connect(
    host='localhost',
    user=userMysql,
    password=passwdMysql,
    database='mytestdb'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()

print(' ')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

mydb = mysql.connector.connect(
    host='localhost',
    user=userMysql,
    password=passwdMysql,
    database='mytestdb'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 3")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()

print(' ')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# join 2 or more tables
# Create the 2 tables for practice
#
# mydb = mysql.connector.connect(
#     host='localhost',
#     user=userMysql,
#     password=passwdMysql,
#     database='mytestdb'
# )
# mycursor = mydb.cursor()
#
# create and populate users table
# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
#
# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#     ('John', '154'),
#     ('Peter', '154'),
#     ('Amy', '155'),
#     ('Hannah', ''),
#     ('Michael', '')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted")
#
#
# create and populate products table also manually edited the id's from this table to 154, 155, 156
# not good practice but it was faster
# mycursor.execute("CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))")  # it failed but created the table???
# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [
#     ('154', 'Chocolate Heaven'),
#     ('155', 'Tasty Lemons'),
#     ('156', 'Vanilla Dreams')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted")
# mydb.close()
#
# print(' ')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# users table:
# { id: 1, name: 'John', fav: 154},
# { id: 2, name: 'Peter', fav: 154},
# { id: 3, name: 'Amy', fav: 155},
# { id: 4, name: 'Hannah', fav:},
# { id: 5, name: 'Michael', fav:}


# products table
# { id: 154, name: 'Chocolate Heaven' },
# { id: 155, name: 'Tasty Lemons' },
# { id: 156, name: 'Vanilla Dreams' }


# These two tables created above can be combined by using users' fav field and products' id field.

mydb = mysql.connector.connect(
    host='localhost',
    user=userMysql,
    password=passwdMysql,
    database='mytestdb'
)

mycursor = mydb.cursor()

# You can use JOIN instead of INNER JOIN. They will both give you the same result.
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"
# prints:
# ('John', 'Chocolate Heaven')
# ('Peter', 'Chocolate Heaven')
# ('Amy', 'Tasty Lemons')


# If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"
# prints:
# ('John', 'Chocolate Heaven')
# ('Peter', 'Chocolate Heaven')
# ('Amy', 'Tasty Lemons')
# ('Hannah', None)
# ('Michael', None)


# If you want to return all products, and the users who have them as their favorite,
# even if no user have them as their favorite, use the RIGHT JOIN statement:
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
# prints:
# ('John', 'Chocolate Heaven')
# ('Peter', 'Chocolate Heaven')
# ('Amy', 'Tasty Lemons')
# (None, 'Vanilla Dreams')

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

mydb.close()

print(' ')

