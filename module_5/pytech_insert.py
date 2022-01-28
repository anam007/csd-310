""" 
    Title: pytech_insert.py
    Author: Anamanno Umanah
    Date: 01/27/2022
    Description: Program for inserting new documents 
                 into the students collection 
"""



#import statement
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.sjyfk.mongodb.net/pytech" 

#connect to mongoDB cluster
client = MongoClient(url)

#connect to pytech database
db =client.pytech

""" three student documents"""
#Alex Gravy's data doc
alex = {
    "student_id": "1007",
    "first_name": "Alex",
    "last_name": "Gravy"
}

#Clinton Warri's doc
clinton = {
    "student_id": "1008",
    "first_name": "Clinton",
    "last_name": "Warri"
}

#Marvis Naija's doc
marvis = {
    "student_id": "1009",
    "first_name": "Marvis",
    "last_name": "Naija"
}

#get the students collection??
students = db.students 

#insert statements 
print ("\n--INSERT STATEMENTS--")
alex_student_id= students.insert_one(alex).inserted_id
print (" Inserted student record Alex Gravy into the students collection with document_id " + str(alex_student_id))

clinton_student_id= students.insert_one(clinton).inserted_id
print (" Inserted student record Clinton Warri into the students collection with document_id " + str(clinton_student_id))

marvis_student_id= students.insert_one(marvis).inserted_id
print (" Inserted student record Marvis Naija into the students collection with document_id " + str(marvis_student_id))


input ( "\n\n End of program, press any key to exit... ")
