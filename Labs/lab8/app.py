from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError

#database setup

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab8.db'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    firstname = db.Column(db.String(50), unique=False, nullable=False)
    lastname = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        try:
            usr = User.query.filter_by(username=username).first()
            if usr.password == password:
                return render_template("secret.html")
            else:
                return render_template("error.html", problem="Username or Password")
        
        except:
                return render_template("error.html", problem="something")
    else:
        return render_template('index.html')


@app.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        Up = False
        Lo = False
        Num = False
        for char in password:
            if char.isupper():
                Up = True
            if char.islower():
                Lo = True
        if password[-1].isnumeric():
            Num = True

        if (password == confirm_password) and Up and Lo and Num:
            new_user = User(username=username, firstname=firstname, lastname=lastname, 
                            email=email, password=password)
            try:
                db.session.add(new_user)
                db.session.commit()

                return render_template("success.html")

            except IntegrityError:
                return render_template("error.html", problem="username or email")
        else:
            return render_template("error.html", problem='Password')
    else:
        return render_template('sign_up.html')


if __name__ == "__main__":
    app.run(debug=True)
