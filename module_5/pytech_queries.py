""" 
    Title: pytech_queries.py
    Author: Anamanno Umanah
    Date: 01/27/2022
    Description: Program for quering documents 
                 in the students collection 
"""

from pymongo import MongoClient

# MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.sjyfk.mongodb.net/pytech" 

#connect to mongoDB cluster
client = MongoClient(url)

#connect to pytech database
db =client.pytech

#get the student collection 
students = db.students

#all students in collection
students_list = students.find({})

#display msg
print ("\n--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")


#loop through collection and output results
for doc in students_list: 
    print ("Student ID:" + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#find one student
clinton = students.find_one({"student_id": "1008"})
print ("\n--DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY--")
print ("Student ID:" + clinton["student_id"] + "\n First Name: " + clinton["first_name"] + "\n Last Name: " + clinton["last_name"] + "\n")

#close progarm msg
input ("\n\n End of program, press any key to exit... ")