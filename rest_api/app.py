from flask import Flask, abort, request
import psycopg2
import psycopg2.extras


# Connect to your postgres DB
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='password',
    host='127.0.0.1',
    port='5432'
)


app = Flask(__name__)

@app.route('/students', methods=['GET'])
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    
    return [dict(student) for student in students]

@app.route('/students/<id>', methods=['GET'])
def show(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM students where id=" + str(id))
    students = cur.fetchall()
    return [dict(student) for student in students]
 

    

# @app.route('/students', methods=['POST'])
# def store():
#     student = {
#         'id': len(records),
#         'name': request.json['name'],
#     }

#     records.append(student)

#     with open('students.json', 'w') as file:
#         json.dump(records, file)

#     return student, 201


if __name__ == '__main__':
    app.run(debug=True)
