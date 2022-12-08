from flask import Flask, abort, request
import json
import os

app = Flask(__name__)

with open(os.path.dirname(__file__) + '/students.json', 'r') as file:
    students = json.load(file) 

@app.route('/students', methods=['GET'])
def index():
    return students

@app.route('/students/<id>', methods=['GET'])
def show(id):
    for student in students:
        if student.get('id') == int(id):
            return student

    return abort(404)

@app.route('/students', methods=['POST'])
def store():
    student = {
        'id': len(students),
        'name': request.json['name'],
    }

    students.append(student)

    with open('students.json', 'w') as file:
        json.dump(students, file) 

    return student, 201


if __name__ == '__main__':
    app.run(debug=True)