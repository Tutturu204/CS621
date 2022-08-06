from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


#app.setup

app.config['SECRET_KEY'] = "Iwillbereadytopassthisprojectontime"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proj.db'

#database setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)
 
from routes import *


if __name__ == '__main__':
    app.run(port=5000, debug=True)
