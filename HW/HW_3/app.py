from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw3_db.db'

#database setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    grade = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        
        student_name = request.form['name']
        student_grade = request.form['grade']
        new_student = Todo(name=student_name, grade=student_grade)

        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue!'
    else:
        # return render_template("index.html")
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:id>")
def delete(id):
    student_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(student_to_delete)
        db.session.commit()
        return redirect("/results")
    except:
        return "There was a problem deleting this task!"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):

    student = Todo.query.get_or_404(id)
    if request.method == 'POST':

        student.grade= request.form['grade']
        student.name= request.form['name']
        try:
            db.session.commit()
            return redirect("/results")

        except:
            return "Some problem with updates"
    else:
        return render_template('update.html', task=student)

@app.route("/results", methods=['POST', 'GET'])
def results():
    students = Todo.query.all()
    return render_template("results.html", tasks=students)

@app.route("/results/score", methods=['POST'])
def score():
    score = request.form['score']
    f_list = []
    students = Todo.query.all()
    for student in students:
        if int(student.grade) > int(score):
            f_list.append(student)
    return render_template("results.html", tasks=f_list)
    
if __name__ == "__main__":
    app.run(debug=True)
