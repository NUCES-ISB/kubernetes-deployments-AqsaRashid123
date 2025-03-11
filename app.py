from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = f"dbname='{os.environ['POSTGRES_DB']}' user='{os.environ['POSTGRES_USER']}' password='{os.environ['POSTGRES_PASSWORD']}' host='postgres-service'"

@app.route("/")
def hello():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Connected to PostgreSQL!", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
