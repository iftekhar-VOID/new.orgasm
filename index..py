import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

init_db()
@app.route("/")
def index():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("index.html", users=users)
@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))

    conn.commit()
    conn.close()

    return redirect("/")
@app.route("/delete/<int:id>")

def delete_user(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update_user(id):
    name = request.form["name"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name=? WHERE id=?", (name, id))

    conn.commit()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
