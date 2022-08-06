from flask import Flask, render_template, url_for, request, redirect, flash
from app import app, db

from models.user import User
from models.course import Course
from sqlalchemy.exc import IntegrityError

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['pwd']

        db_password = User.query.filter_by(email=email).first().password

        if (password == db_password) :
            flash('You were successfully Logged in')
            return render_template("home.html", category="success")
        else:
            flash('Check your data again')
            return render_template("index.html", category="warning")
    
    if request.method == 'GET':
        return render_template("index.html")

@app.route("/registration", methods=['GET', 'POST'])
def registartion():
    if request.method == 'POST':

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['pwd']

        new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('You were successfully sign in')
            return redirect("/")

        except IntegrityError:
            return render_template("error.html", problem="email")
    else:
        return render_template("registration.html", category="success")

@app.route("/library", methods=['GET'])
def library():
    
    if request.method == 'GET':
        course_list = Course.query.all()
        return render_template("library.html", rows=course_list)


@app.route("/home", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['pwd']

        db_password = User.query.filter_by(email=email).first().password

        if (password == db_password) :
            flash('You were successfully Logged in')
            return render_template("home.html", category="success")
        else:
            flash('Check your data again')
            return render_template("index.html", category="warning")
    
    if request.method == 'GET':
        return render_template("home.html")

@app.route("/add", methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':

        name = request.form['name']
        professor = request.form['professor']
        semester = request.form['semester']
        score = request.form['score']
        weight = request.form['weight']
        description = request.form['description']

        new_course = Course(name=name, professor=professor, semester=semester, score=score, weight=weight, description=description)
            
        try:
            db.session.add(new_course)
            db.session.commit()
            flash('Course has been added!')
            return render_template("home.html", category='success')

        except IntegrityError:
            return render_template("error.html", problem="fields")    

    if request.method == 'GET':
        return render_template("add.html")

@app.route("/update", methods=['GET', 'POST'])
def update():
    
    if request.method == 'POST':

        course_id = request.form['course_id']
        course = Course.query.get_or_404(course_id)
        if course:
            flash('Course Founded!')
            return render_template("update_concrete.html", category='success', course=course)

        else:
            flash('Something goes wrong!')
            return render_template("update.html", category='warning')    

    if request.method == 'GET':
        return render_template("update.html")


@app.route("/update/<int:course_id>", methods=['GET', 'POST'])
def update_concrete(course_id):
    
    if request.method == 'POST':
        course = Course.query.get_or_404(course_id)

        course.name = request.form['name']
        course.professor = request.form['professor']
        course.semester = request.form['semester']
        course.score = request.form['score']
        course.weight = request.form['weight']
        course.description = request.form['description']
    
        try:
            db.session.commit()
            flash('Course has been changed!')
            return render_template("home.html", category='success')

        except:
            flash('Something goes wrong!')
            return render_template("update_concrete.html", category='warning')    

    if request.method == 'GET':
        return render_template("update_concrete.html")

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    
    if request.method == 'POST':

        course_id = request.form['course_id']

        course = Course.query.get(course_id)
            
        try:
            db.session.delete(course)
            db.session.commit()
            flash('Course has been deleted!')
            return render_template("home.html", category='success')

        except:
            flash('Something goes wrong!')
            return render_template("delete.html", category='warning')    

    if request.method == 'GET':
        return render_template("delete.html")


@app.route("/generate", methods=['GET'])
def generate():
    
    if request.method == 'GET':
        third_courses = Course.query.filter_by(score=3).all()
        second_courses = Course.query.filter_by(score=2).all()
        first_courses = Course.query.filter_by(score=1).all()
        
        summer_courses = Course.query.filter_by(semester="Summer").all()

        fall_third_courses = []
        fall_second_courses = []
        fall_first_courses = []

        spring_third_courses = []
        spring_second_courses = []
        spring_first_courses = []

        for course in third_courses:
            if course.semester == 'Fall':
                fall_third_courses.append(course)
            if course.semester == 'Spring':
                spring_third_courses.append(course) 

        for course in second_courses:
            if course.semester == 'Fall':
                fall_second_courses.append(course)
            if course.semester == 'Spring':
                spring_second_courses.append(course)   

        for course in first_courses:
            if course.semester == 'Fall':
                fall_first_courses.append(course)
            if course.semester == 'Spring':
                spring_first_courses.append(course)

        fall_courses = []      
        
        if fall_third_courses:
            fall_courses.append(fall_third_courses[0])
            fall_third_courses.pop(0)
        elif fall_second_courses:
            fall_courses.append(fall_second_courses[0])
            fall_second_courses.pop(0)
        elif fall_first_courses:
            fall_courses.append(fall_first_courses[0])
            fall_first_courses.pop(0)

        if fall_second_courses:
            fall_courses.append(fall_second_courses[0])
            fall_second_courses.pop(0)
        elif fall_first_courses:
            fall_courses.append(fall_first_courses[0])
            fall_first_courses.pop(0)

        if fall_first_courses:
            fall_courses.append(fall_first_courses[0])
            fall_first_courses.pop(0)    
        elif fall_second_courses:
            fall_courses.append(fall_second_courses[0])
            fall_second_courses.pop(0)

        spring_courses = []      
        
        if spring_third_courses:
            spring_courses.append(spring_third_courses[0])
            spring_third_courses.pop(0)
        elif spring_second_courses:
            spring_courses.append(spring_second_courses[0])
            spring_second_courses.pop(0)
        elif springfirst_courses:
            spring_courses.append(spring_first_courses[0])
            spring_first_courses.pop(0)

        if spring_second_courses:
            spring_courses.append(spring_second_courses[0])
            spring_second_courses.pop(0)
        elif spring_first_courses:
            spring_courses.append(spring_first_courses[0])
            springfirst_courses.pop(0)

        if spring_first_courses:
            spring_courses.append(spring_first_courses[0])
            spring_first_courses.pop(0)    
        elif spring_second_courses:
            spring_courses.append(spring_second_courses[0])
            spring_second_courses.pop(0)

        second_fall_courses = []      
        
        if fall_third_courses:
            second_fall_courses.append(fall_third_courses[0])
            fall_third_courses.pop(0)
        elif fall_second_courses:
            second_fall_courses.append(fall_second_courses[0])
            fall_second_courses.pop(0)
        elif fall_first_courses:
            second_fall_courses.append(fall_first_courses[0])
            fall_first_courses.pop(0)

        if fall_second_courses:
            second_fall_courses.append(fall_second_courses[0])
            fall_second_courses.pop(0)
        elif fall_first_courses:
            second_fall_courses.append(fall_first_courses[0])
            fall_first_courses.pop(0)

        if fall_first_courses:
            second_fall_courses.append(fall_first_courses[0])
            fall_first_courses.pop(0)    
        elif fall_second_courses:
            second_fall_courses.append(fall_second_courses[0])
            fall_second_courses.pop(0)

        return render_template("generate.html", fall_courses=fall_courses, spring_courses=spring_courses, summer_courses=summer_courses, second_fall_courses=second_fall_courses)








