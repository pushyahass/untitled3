import os
from flask import Flask, render_template, request
import sqlite3
import csv

app = Flask(__name__)

with open('static/People.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter =',')

    for row in csvfile:
        print (row)

conn = sqlite3.connect('people.db')
cur = conn.cursor()
print("Database created successfully")

cur.execute('CREATE TABLE IF NOT EXISTS people (name TEXT, grade TEXT, room TEXT, telnum REAL, picture BLOB, keywords TEXT)')
print("Table created successfully")

reader = csv.reader(open('static/people.csv', 'r') )
for row in reader:
    to_db = [row[0], row[1], row[2], row[3], row[4], row[5]]
    cur.execute("INSERT INTO people (name, grade,room,telnum,picture,keywords) VALUES (?, ?, ?,? ,? ,?);", to_db)
conn.commit()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    loc = os.path.join(APP_ROOT, 'static/')
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

@app.route("/search", methods=['POST'])
def search():
    cur.execute("SELECT picture FROM people WHERE name='Nora'")
    image = cur.fetchall()
    image = image[0][0]
    print(image[0][0])
    #image = 'Jees.jpg'
    return render_template("searchimg.html", image_name=image)

if __name__ == '__main__':
   app.run()
