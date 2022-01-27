""" 
    Title: mongodb_test.py
    Author: Anamanno Umanah 
    Date: 26 Jan 2022
    Description: Test program for connecting to a 
                 MongoDB Atlas cluster
"""
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.sjyfk.mongodb.net/pytech" 

client = MongoClient(url)

db =client.pytech 

print("\n -- Pytech COllection List --")
print (db.list_collection_names())

input("\n End of program, press any key to exit... ")

