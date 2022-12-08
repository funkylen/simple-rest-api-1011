from flask import Flask, abort, request
import psycopg2
import psycopg2.extras


def get_db():

    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='password',
        host='127.0.0.1',
        port='5432'
    )
    return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


app = Flask(__name__)


@app.route('/students', methods=['GET'])
def index():
    cur = get_db()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    return [dict(student) for student in students]


@app.route('/students/<id>', methods=['GET'])
def show(id):
    cur = get_db()
    cur.execute("SELECT * FROM students where id = %s", (id))

    student = cur.fetchone()

    return dict(student)


@app.route('/students', methods=['POST'])
def store():
    cur = get_db()
    name = request.json['name']

    cur.execute("INSERT INTO students (name) values (%s) RETURNING *", (name,))

    student = cur.fetchone()
    return dict(student)


if __name__ == '__main__':
    app.run(debug=True)
