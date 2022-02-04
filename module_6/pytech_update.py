""" 
    Title: pytech_update.py
    Author: Anamanno Umanah
    Date: 02/03/2022
    Description: Program for updating documents 
                 in students collection 
"""

#import statement
from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.sjyfk.mongodb.net/pytech" 

#connect to mongoDB cluster
client = MongoClient(url)

#connect to pytech database
db =client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for student_doc in student_list:
    print("  Student ID: " + student_doc["student_id"] + "\n  First Name: " + student_doc["first_name"] + "\n  Last Name: " + student_doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Windslow"}})

# find the updated student document 
alex = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + alex["student_id"] + "\n  First Name: " + alex["first_name"] + "\n  Last Name: " + alex["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
