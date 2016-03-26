#parsed mbox

import sqlite3
conn = sqlite3.connect('coursera_db.sqlite')

cur = conn.cursor()

cur.execute(''' DROP TABLE IF EXISTS Counts ''' )
cur.execute('CREATE TABLE Counts (org TEXT , count INTEGER)')


flname = raw_input ("Enter file name (1 - mbox.txt, 2 - mbox-short.txt) :")

if flname == '1':
	flname = 'mbox.txt'
elif flname == '2':
	flname = 'mbox-short.txt'
else:
	print ('Ok, file name is ', flname)



opn_fl = open (flname)


for line in opn_fl:
	if not line.startswith('From: ') :
		continue

	pieces = line.split()
	email = pieces[1]
	index = email.index('@')
	org = email[index+1:]
	

	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
	row = cur.fetchone()
	if row is None:
		cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

	conn.commit()

slqstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5"
print 
print "Counts:"
for i in cur.execute(slqstr):
	print str(i[0]), i[1]

cur.close()


	


