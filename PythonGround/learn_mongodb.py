import pymongo


# In MongoDB, a database is not created until it gets content!
# MongoDB waits until you have created a collection (table), with at least one document (record)
# before it actually creates the database (and collection).

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
# # mydict = {"name": "John", "address": "Highway 37"}  # disable after first run so you dont enter duplicates
#
# mydict1 = {"name": "Peter", "address": "Lowstreet 27"}  # If you do not specify an _id field,
#                                                         # then MongoDB will add one for you and assign
#                                                         # a unique id for each document
#
# # x = mycol.insert_one(mydict)  # disable if mydict is commented out
# x1 = mycol.insert_one(mydict1)
#
# print(x1.inserted_id)
#
# print(myclient.list_database_names())
#
#
# # you can check a specific database by name:
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The databse exists")
#
# # you can check a specific collection by name:
# collist = mydb.list_collection_names()
# if "customers" in collist:
#     print("The collection exists!")

# ======================================================================================================================

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]
#
# mylist = [
#     {"name": "Amy", "address": "Apple st 652"},
#     {"name": "Hannah", "address": "Mountain 21"},
#     {"name": "Michael", "address": "Valley 345"},
#     {"name": "Sandy", "address": "Ocean blvd 2"},
#     {"name": "Betty", "address": "Green Grass 1"},
#     {"name": "Richard", "address": "Sky st 331"},
#     {"name": "Susan", "address": "One way 98"},
#     {"name": "Vicky", "address": "Yellow Garden 2"},
#     {"name": "Ben", "address": "Park Lane 38"},
#     {"name": "William", "address": "Central st 954"},
#     {"name": "Chuck", "address": "Main Road 989"},
#     {"name": "Viola", "address": "Sideway 1633"}
# ]
#
# mylist1 = [
#     {"_id": 1, "name": "John", "address": "Highway 37"},
#     {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#     {"_id": 3, "name": "Amy", "address": "Apple st 652"},
#     {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
#     {"_id": 5, "name": "Michael", "address": "Valley 345"},
#     {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#     {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
#     {"_id": 8, "name": "Richard", "address": "Sky st 331"},
#     {"_id": 9, "name": "Susan", "address": "One way 98"},
#     {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#     {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
#     {"_id": 12, "name": "William", "address": "Central st 954"},
#     {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
#     {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
#
# # x = mycol.insert_many(mylist)
# x1 = mycol.insert_many(mylist1)
#
# # print list of the _id values of the inserted documents
# # insert_many() method returns a InsertManyResult object, which has a property, inserted_ids,
# # that holds the ids of the inserted documents
#
# # print(x.inserted_ids)
# print(x1.inserted_ids)

# ======================================================================================================================

# myclient = pymongo.MongoClient("mongodb://localhost:27017")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# x = mycol.find_one()  # returns the first occurrence in the selection
# print(x)


# find() method returns all occurrences in the selection
# The first parameter of the find() method is a query object
# No parameters in the find() method gives you the same result as SELECT * in MySQL

# for x in mycol.find():
#     print(x)
#
# print("=" * 50)  # separator  between prints in console


# The second parameter of the find() method is an object describing which fields to include in the result
# This parameter is optional, and if omitted, all fields will be included in the result

# for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
#     print(x)
#
# print("=" * 50)  # separator  between prints in console

# You are not allowed to specify both 0 and 1 values in the same object
# (except if one of the fields is the _id field). If you specify a field with the value 0,
# all other fields get the value 1, and vice versa

# for x in mycol.find({}, {"address": 0}):  # exclude "address" from the result
#     print(x)

# ======================================================================================================================

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)


print("=" * 50)  # separator  between prints in console

# To make advanced queries you can use modifiers as values in the query object
# to find the documents where the "address" field starts with the letter "S" or higher (alphabetically),
# use the greater than modifier: {"$gt": "S"}

myquery1 = {"address": {"$gt": "S"}}  # find documents where the address starts with the letter "S" or higher
mydoc1 = mycol.find(myquery1)

for x in mydoc1:
    print(x)


print("=" * 50)  # separator  between prints in console

# You can also use regular expressions as a modifier
# Regular expressions can only be used to query strings

myquery2 = {"address": {"$regex": "^S"}}
mydoc2 = mycol.find(myquery2)

for x in mydoc2:
    print(x)


print("=" * 50)  # separator  between prints in console

# Use the sort() method to sort the result in ascending or descending order.
# The sort() method takes one parameter for "fieldname" and one parameter
# for "direction" (ascending is the default direction).

mydoc3 = mycol.find().sort("name")
for x in mydoc3:
    print(x)


print("=" * 50)  # separator  between prints in console

# Use the value -1 as the second parameter to sort descending
# sort("name", 1) #ascending
# sort("name", -1) #descending

mydoc4 = mycol.find().sort("name", -1)

for x in mydoc4:
    print(x)


print("=" * 50)  # separator  between prints in console

# ======================================================================================================================

# first parameter of the delete_one() method is a query object defining which document to delete
# If the query finds more than one document, only the first occurrence is deleted
#
# myquery = {"address": "Mountain 21"}  # Delete the document with the address "Mountain 21"
# mycol.delete_one(myquery)


# first parameter of the delete_many() method is a query object defining which documents to delete
#
# myquery = {"address": {"$regex": "^S"}}  # Delete all documents were the address starts with the letter S
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")


# delete all documents in a collection, pass an empty query object to the delete_many() method
#
# x = mycol.delete_many({})  # delete all documents in the "customers" collection
# print(x.deleted_count, " documents deleted.")


# You can delete a table, or collection as it is called in MongoDB, by using the drop() method
# drop() method returns true if the collection was dropped successfully, and false if the collection does not exist
# mycol.drop()


# ======================================================================================================================


# update a record, or document as it is called in MongoDB, by using the update_one() method
# first parameter of the update_one() method is a query object defining which document to update
# If the query finds more than one record, only the first occurrence is updated.
# second parameter is an object defining the new values of the document.

# myquery3 = {"address": "Valley 345"}
# newvalues = {"$set": {"address": "Canyon 123"}}
# mycol.update_one(myquery3, newvalues)  # Change the address from "Valley 345" to "Canyon 123"
#
# for x in mycol.find():
#     print(x)


# update all documents that meets the criteria of the query, use the update_many() method

# myquery4 = {"address": {"$regex": "^S"}}
# newvalues1 = {"$set": {"name": "Minnie"}}
#
# x = mycol.update_many(myquery4, newvalues1)
#
# print(x.modified_count, "documents updated.")


# limit() method takes one parameter, a number defining how many documents to return
myresultA = mycol.find().limit(5)

# print the result:
for x in myresultA:
    print(x)

