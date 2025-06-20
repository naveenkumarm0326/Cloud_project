import pymongo
from pymongo import MongoClient

# MongoDB Connection
try:
    client = MongoClient("mongodb+srv://naveenkumarm0312:KBzn7zsYVUo9PFVp@cluster0.671qd.mongodb.net/")
    client.admin.command('ping')
    print(" Connected to MongoDB successfully!")
except Exception as e:
    print("X Error connecting to MongoDB:", e)
    exit() # Exit script if connection fails

# Database & Collection
db = client["student"]
students_collection = db ["student"] # Ensure this matches your actual collection name

# Student Data
student_data = {
    "student_id": "12", # Ensure uniqueness
    "name": "vaaaaa",
    "DOB": "13-12-2000",
    "age": 23,
    "department": "DSA",
    "courses": ["DS", "LAB", "MINI PROJECT"],
    "GPA": 9.4
}

# Insert Data with Duplicate Check
if students_collection.find_one({"student_id": student_data["student_id"]}):
    print(f" Student ID {student_data['student_id']} already exists. Not inserting.")
else:
    result = students_collection.insert_one(student_data)
    print(f" Student data inserted with ID: {result.inserted_id}")



























