from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "college_dbms_secret"
# -------------------------------------------------
# MYSQL CONNECTION
# -------------------------------------------------

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ashwin123',
    database='college_db'
)

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

@app.route('/')
def home():

    cursor = connection.cursor()

    # Fetch student data

    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    # Dashboard Counts

    cursor.execute("SELECT COUNT(*) FROM student")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM courses")
    total_courses = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM instructor")
    total_instructors = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM department")
    total_departments = cursor.fetchone()[0]

    cursor.close()

    return render_template(
        'index.html',
        students=students,
        total_students=total_students,
        total_courses=total_courses,
        total_instructors=total_instructors,
        total_departments=total_departments
    )

# -------------------------------------------------
# INSTRUCTORS PAGE
# -------------------------------------------------

@app.route('/instructors')
def instructors():

    cursor = connection.cursor()

    # Fetch instructors

    cursor.execute("SELECT * FROM instructor")
    instructors = cursor.fetchall()

    # Fetch departments for dropdown

    cursor.execute("SELECT * FROM department")
    departments = cursor.fetchall()

    cursor.close()

    return render_template(
        'instructors.html',
        instructors=instructors,
        departments=departments
    )

# -------------------------------------------------
# INSERT INSTRUCTOR
# -------------------------------------------------

@app.route('/add_instructor', methods=['POST'])
def add_instructor():

    cursor = connection.cursor()

    instructor_id = request.form['instructor_id']
    instructor_name = request.form['instructor_name']
    department_id = request.form['department_id']

    query = """
    INSERT INTO instructor
    (instructor_id, instructor_name, department_id)
    VALUES (%s, %s, %s)
    """

    values = (
        instructor_id,
        instructor_name,
        department_id
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    flash("Instructor added successfully!", "success")

    return redirect(url_for('instructors'))

# -------------------------------------------------
# DELETE INSTRUCTOR
# -------------------------------------------------

@app.route('/delete_instructor/<int:instructor_id>')
def delete_instructor(instructor_id):

    cursor = connection.cursor()

    try:

        # First remove related courses

        course_query = """
        DELETE FROM courses
        WHERE instructor_id = %s
        """

        cursor.execute(course_query, (instructor_id,))

        # Then remove instructor

        instructor_query = """
        DELETE FROM instructor
        WHERE instructor_id = %s
        """

        cursor.execute(instructor_query, (instructor_id,))

        connection.commit()

    except Exception as e:

        print(e)

    finally:

        cursor.close()

    flash("Instructor deleted successfully!", "danger")
    return redirect(url_for('instructors'))

# -------------------------------------------------
# STUDENTS PAGE
# -------------------------------------------------

@app.route('/students')
def students():

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    cursor.close()

    return render_template(
        'students.html',
        students=students
    )

# -------------------------------------------------
# ADD STUDENT PAGE
# -------------------------------------------------

@app.route('/add_student')
def add_student():

    return render_template(
        'add_student.html'
    )

# -------------------------------------------------
# INSERT STUDENT
# -------------------------------------------------

@app.route('/insert_student', methods=['POST'])
def insert_student():

    cursor = connection.cursor()

    student_id = request.form['student_id']
    student_name = request.form['student_name']
    year = request.form['year']
    age = request.form['age']
    address = request.form['address']

    query = """
    INSERT INTO student
    (student_id, student_name, year, age, address)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        student_id,
        student_name,
        year,
        age,
        address
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()

    flash("Student added successfully!", "success")

    return redirect(url_for('students'))

# -------------------------------------------------
# DELETE STUDENT
# -------------------------------------------------

@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):

    cursor = connection.cursor()

    # Delete related enrollment records first

    enrollment_query = """
    DELETE FROM enrollment
    WHERE student_id = %s
    """

    cursor.execute(enrollment_query, (student_id,))

    # Then delete student

    student_query = """
    DELETE FROM student
    WHERE student_id = %s
    """

    cursor.execute(student_query, (student_id,))

    connection.commit()

    cursor.close()
    flash("Student deleted successfully!", "danger")

    return redirect(url_for('students'))

# -------------------------------------------------
# COURSES PAGE
# -------------------------------------------------

@app.route('/courses')
def courses():

    cursor = connection.cursor()

    # Fetch courses

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    # Fetch departments

    cursor.execute("SELECT * FROM department")
    departments = cursor.fetchall()

    # Fetch instructors

    cursor.execute("SELECT * FROM instructor")
    instructors = cursor.fetchall()

    cursor.close()

    return render_template(
        'courses.html',
        courses=courses,
        departments=departments,
        instructors=instructors
    )

# -------------------------------------------------
# ADD COURSE
# -------------------------------------------------

@app.route('/add_course', methods=['POST'])
def add_course():

    cursor = connection.cursor()

    course_id = request.form['course_id']
    course_name = request.form['course_name']
    department_id = request.form['department_id']
    instructor_id = request.form['instructor_id']
    course_duration = request.form['course_duration']

    query = """
    INSERT INTO courses
    (course_id, course_name, department_id, instructor_id, course_duration)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        course_id,
        course_name,
        department_id,
        instructor_id,
        course_duration
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    flash("Course added successfully!", "success")

    return redirect(url_for('courses'))

# -------------------------------------------------
# DELETE COURSE
# -------------------------------------------------

@app.route('/delete_course/<int:course_id>')
def delete_course(course_id):

    cursor = connection.cursor()

    # First delete related enrollments

    enrollment_query = """
    DELETE FROM enrollment
    WHERE course_id = %s
    """

    cursor.execute(enrollment_query, (course_id,))

    # Then delete course

    course_query = """
    DELETE FROM courses
    WHERE course_id = %s
    """

    cursor.execute(course_query, (course_id,))

    connection.commit()

    cursor.close()
    flash("Course deleted successfully!", "danger")

    return redirect(url_for('courses'))

# -------------------------------------------------
# ENROLLMENT PAGE
# -------------------------------------------------

@app.route('/enrollment')
def enrollment():

    cursor = connection.cursor()

    # Enrollment table data

    query = """
    SELECT
    student.student_name,
    courses.course_name,
    enrollment.student_id,
    enrollment.course_id
    FROM enrollment
    JOIN student
    ON enrollment.student_id = student.student_id
    JOIN courses
    ON enrollment.course_id = courses.course_id
    """

    cursor.execute(query)

    enrollments = cursor.fetchall()

    # Fetch students for dropdown

    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    # Fetch courses for dropdown

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    cursor.close()

    return render_template(
        'enrollment.html',
        enrollments=enrollments,
        students=students,
        courses=courses
    )

# -------------------------------------------------
# ADD ENROLLMENT
# -------------------------------------------------

@app.route('/add_enrollment', methods=['POST'])
def add_enrollment():

    cursor = connection.cursor()

    student_id = request.form['student_id']
    course_id = request.form['course_id']

    query = """
    INSERT INTO enrollment
    (student_id, course_id)
    VALUES (%s, %s)
    """

    values = (
        student_id,
        course_id
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    flash("Enrollment added successfully!", "success")

    return redirect(url_for('enrollment'))

# -------------------------------------------------
# DELETE ENROLLMENT
# -------------------------------------------------

@app.route('/delete_enrollment/<int:student_id>/<int:course_id>')
def delete_enrollment(student_id, course_id):

    cursor = connection.cursor()

    query = """
    DELETE FROM enrollment
    WHERE student_id = %s
    AND course_id = %s
    """

    values = (
        student_id,
        course_id
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    flash("Enrollment deleted successfully!", "danger")

    return redirect(url_for('enrollment'))

# -------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5050)