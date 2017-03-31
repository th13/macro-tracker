from os import environ
import time
import logging

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# TODO: Refactor code into multiple files.
# from models import *

app = Flask(__name__)

# TODO: Figure out why the provided logger in Flask doesn't output on Docker
# container.
logger = logging.getLogger("api")
logger.setLevel(logging.INFO)
logger_handler = logging.StreamHandler()
logger_handler.setLevel(logging.INFO)
logger_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(logger_handler)


connection_info = {
    "user": environ["POSTGRES_USER"],
    "password": environ["POSTGRES_PASSWORD"],
    "db": environ["POSTGRES_DB"]
}

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://{user}:{password}@db:5432/{db}".format(**connection_info)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email
            }

# Attempt to connect to the database and create tables.
while True:
    try:
        db.create_all()
    except Exception as e:
        logger.warning("Retrying database connection...")
        time.sleep(3)
    else:
        logger.info("Database connection established.")
        break


@app.route("/", methods=["POST", "GET"])
def default():
    return "Welcome to the Macro Tracker API."

@app.route("/user", methods=["POST"])
def create_user():
    formName = request.form["name"]
    formEmail = request.form["email"]
    u = User(formName, formEmail)
    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())

@app.errorhandler(Exception)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")