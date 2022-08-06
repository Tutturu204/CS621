from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw4_db.db'

#database setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email =  db.Column(db.String(60), nullable=False)
    phone =  db.Column(db.String(20), nullable=False)
    adress =  db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return f"Record name: {self.name}, email: {self.email}, phone: {self.phone}, adress: {self.adress}"

@app.route("/", methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        adress = request.form['adress']
        
        new_record = Records(name=name, email=email, phone=phone, adress=adress)

        try:
            db.session.add(new_record)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue!'
    else:
        return render_template("index.html")

@app.route("/delete/<int:id>")
def delete(id):
    record = Records.query.get_or_404(id)
    try:
        db.session.delete(record)
        db.session.commit()
        return redirect("/results")
    except:
        return "There was a problem deleting this task!"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):

    record = Records.query.get_or_404(id)
    if request.method == 'POST':

        record.name = request.form['name']
        record.email = request.form['email']
        record.phone = request.form['phone']
        record.adress = request.form['adress']

        try:
            db.session.commit()
            return redirect("/results")

        except:
            return "Some problem with updates"
    else:
        return render_template('update.html', task=record)

@app.route("/results", methods=['POST', 'GET'])
def results():
    records = Records.query.all()
    return render_template("results.html", tasks=records)

  
if __name__ == "__main__":
    app.run(debug=True)
