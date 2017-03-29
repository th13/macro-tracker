from os import environ

from flask import Flask
import sqlalchemy
import time
import logging

app = Flask(__name__)

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

connection_string = "postgres+psycopg2://{user}:{password}@db:5432/{db}".format(**connection_info)

db = None
engine = None
meta = None

# Attempt to connect to the database.
while True:
    try:
        db = sqlalchemy.create_engine(connection_string)
        engine = db.connect()
        meta = sqlalchemy.MetaData(engine)
    except Exception as e:
        logger.warning("Retrying database connection...")
        time.sleep(5)
    else:
        logger.info("Database connection established.")
        break


@app.route("/", methods=["POST", "GET"])
def default():
    return "Welcome to the Macro Tracker API."


if __name__ == "__main__":
    app.run(host="0.0.0.0")