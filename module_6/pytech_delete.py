""" 
    Title: pytech_delete.py
    Author: Anamanno Umanah
    Date: 02/03/2022
    Description: Program for deleting documents 
                 in students collection 
"""

#import statement
from pymongo import MongoClient

#MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.sjyfk.mongodb.net/pytech" 

#connect to mongoDB cluster
client = MongoClient(url)

#connect to pytech database
db =client.pytech

#get the students collection 
students = db.students

#find all students in the collection 
student_list = students.find({})

#display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#new document 
new_student = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Johnson"
}

#insert the new document into MongoDB atlas 
new_doc_id = students.insert_one(new_student).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_doc_id))

#call the find_one() method by student_id 1010
new_student_doc = students.find_one({"student_id": "1010"})

#display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + new_student_doc["student_id"] + "\n  First Name: " + new_student_doc["first_name"] + "\n  Last Name: " + new_student_doc["last_name"] + "\n")

#call the delete_one method to remove the new_student_doc
deleted_new_student_doc = students.delete_one({"student_id": "1010"})

#find all students in the collection 
new_student_list = students.find({})

#display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#exit message 
input("\n\n  End of program, press any key to continue...")