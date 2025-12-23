import flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3

app = flask.Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day"],
    storage_uri="memory://",
)

conn = sqlite3.connect('gifts.db') 
cursor = conn.cursor()  
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gifts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class TEXT NOT NULL
    )
''')
conn.commit()  
conn.close()

@app.get("/")
@limiter.exempt
def index():
    return flask.send_from_directory("static", "index.html")

@app.post("/hw")
@limiter.limit("1 per second")
def createHW():
    data = flask.request.get_json()
    name = date.get("name")
    schoolClass = data.get("class")

    conn = sqlite3.connect("gifts.db")
    cursor.execute('INSERT INTO gifts (name, class) VALUES (?, ?)', (name, schoolClass))
    conn.commit()
    con.close()

    return "", 201

@app.get("/hw")
@limiter.limit("1 per second")
def getHW():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, class FROM gifts')
    rows = cursor.fetchall()
    conn.close()

    hwStuff = [{'id': row[0], 'name': row[1], 'class': row[2]} for row in rows]

    return flask.jsonify(hwStuff)

if __name__ == "__main__":
    app.run()