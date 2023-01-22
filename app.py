from flask import Flask, render_template
import requests
import sqlite3

app = Flask(__name__)

#@app.route("/")
#def hello_world():
    #return render_template("index.html")

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row 
    return conn 

@app.route("/")
def index():
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()
    return render_template('index.html', projects=projects)