from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        
        name = request.form['name']
        password = request.form['password']
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
        
        if Up and Lo and Num:    
            return render_template('report.html')
        else:
            return render_template('error.html')
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
