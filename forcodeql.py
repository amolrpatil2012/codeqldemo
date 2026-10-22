from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username ss")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    conn.execute(query)
    return "Done"
