import os
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

#import sqlite3
#conn = sqlite3.connect('database.db')

# print("Opened database successfully")

# conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
# print("Table created successfully")
# conn.close()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    loc = os.path.join(APP_ROOT, 'csvfile/')
    print(loc)

    if not os.path.isdir(loc):
        os.mkdir(loc)

    for file in request.files.getlist("file"):
        print (file)
        filename = file.filename
        dest_loc = "/".join([loc, filename])
        print(dest_loc)
        file.save(dest_loc)

    return render_template("success.html")

if __name__ == '__main__':
    app.run()
