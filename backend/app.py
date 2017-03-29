from flask import Flask
import sqlalchemy
import time
import logging

connection_string = "postgres+psycopg2://superfit:Sm4llBlu3F1sh@db:5432/macrotracker"

app = Flask(__name__)

logger = logging.getLogger("api")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

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
        logger.info("Retrying database connection...")
        time.sleep(5)
    else:
        logger.info("Database connection established.")
        break
        

@app.route("/", methods=["POST", "GET"])
def default():
    return "Welcome to the Macro Tracker backend API."

@app.route("/test", methods=["GET"])
def test():
    result = engine.execute("SELECT 1")
    return "result {}".format(result.rowcount)


if __name__ == "__main__":
    app.run(host="0.0.0.0")