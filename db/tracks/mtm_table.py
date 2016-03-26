import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Create ot Refresh tables
#TODO Run as the script or one by one..

cur.executescript(
'''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE );
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE , title TEXT UNIQUE );
CREATE TABLE Member (user_id INTEGER , course_id INTEGER , role INTEGER , PRIMARY KEY (user_id, course_id))
'''
)

fname = raw_input('Enter file name or "Enter" button to use default file :\n')
if len(fname) < 1:
    fname = 'roster_data.json'
print 'File name is "{}"'.format(fname), "\nContinue.."

str_data = open(fname).read()
js_data = json.loads(str_data)

for entry in js_data:
    name = entry[0]
    title = entry[1]
    role = int(entry[2])
    print name,title, role

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id =cur.fetchone()[0]



    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, role))

    conn.commit()
