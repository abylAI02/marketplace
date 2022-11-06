from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

# app object (literally web server)
app = Flask(__name__)



# # Adding SQLite3 database URI to a config
# app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:/AITU/AITU 2022-23/Trimester 1/AP 1 Python/Lectures/Lecture Examples/Lecture 7 - Code Examples/Lecture 6 going 7 - Complex Example V3/lecture6db.db'

# # Adding PostgreSQL database URI to a config
# # pip install psycopg2
# app.config['SQLALCHEMY_DATABASE_URI'] = r"postgresql://postgres:postgres@localhost:5432/lecture7pt2"

# Adding PostgreSQL database URI to a config
# pip install pymysql
app.config['SQLALCHEMY_DATABASE_URI'] = r'postgresql://postgres:root@localhost:5432/lecture7pt2'

with app.app_context():
    db.init_app(app)

# Used to create a session object
# user can look at the session contents, but can’t modify it 
# unless they know the secret key, so make sure to set that to something complex and unguessable.
app.config['SECRET_KEY']="my secret key here"

