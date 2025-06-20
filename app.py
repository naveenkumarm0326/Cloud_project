from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pymongo

app = Flask(__name__, template_folder="templates")
CORS(app)

# Connect to MongoDB Atlas
try:
    client = pymongo.MongoClient("mongodb-srv://naveenkumarm0312:KBzn7zsYVUo9PFVp@cluster8.671qd.mongodb.net/")
    db = client.get_database("student")
    students_collection = db["student"]
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("X Error connecting to MongoDB:", e)

# Route to serve the frontend
@app.route('/')
def home():
    return render_template("index.html")

#API to insert student data
@app.route('/insert', methods=['POST'])
def insert_student():
    data = request.json
    if not data or "student_id" not in data:
        return jsonify(("error": "Invalid data")), 400

    existing_student = students_collection.find_one({"student_id": data["student_id"]})
    if existing_student:
        return jsonify(("error": "Student already exists")), 480

    students_collection.insert_one(data)
    return jsonify({"message": "Student inserted successfully!"}), 201

#API to retrieve student data by student_id
@app.route("/student", methods=['GET'])
def get_student():
    student_id = request.args.get("id")
    if not student_id:
        return jsonify(("error": "Student ID required")), 400

    student = students_collection.find_one({"student_id": student_id}, {"_id": 0}) # Exclude MongoDB _id field
    if not student:
        return jsonify(("error": "Student not found")), 404

    return jsonify(student)

if __name__ == '__main__':
    app.run(debug=True)

