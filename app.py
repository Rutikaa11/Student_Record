from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/students', methods=['GET', 'POST'])
def student_list():
    if request.method == 'POST':
        # Add new student
        name = request.form.get('name')
        age = request.form.get('age')
        grade = request.form.get('grade')
        if name and age and grade:
            students.append({'name': name, 'age': age, 'grade': grade})
        return redirect(url_for('student_list'))

    return render_template('students.html', students=students)

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    if 0 <= student_id < len(students):
        students.pop(student_id)
    return redirect(url_for('student_list'))

@app.route('/update/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_age = request.form.get('age')
        new_grade = request.form.get('grade')
        if 0 <= student_id < len(students) and new_name and new_age and new_grade:
            students[student_id] = {'name': new_name, 'age': new_age, 'grade': new_grade}
        return redirect(url_for('student_list'))

    student_to_update = students[student_id] if 0 <= student_id < len(students) else None
    return render_template('update_student.html', student=student_to_update, student_id=student_id)

if __name__ == '__main__':
    app.run(debug=True)
