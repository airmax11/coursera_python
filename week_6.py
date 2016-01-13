'''
10.2 Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each 
of the messages. You can pull the hour out from the 'From ' 
line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''


get_name  = raw_input ("Enter file name: ")

if len(get_name) < 1:
	get_name = 'mbox-short.txt'

flop = open (get_name)

time = dict()

test = list()

for i in flop:
	if i.startswith ('From '):
		tmp = i.split()
		test.append(tmp[5])

tets3 = list()

for i in test:
	tmp = i.split(':')
	tets3.append(tmp[0])


for i in tets3:
	time[i] = time.get(i, 0) + 1

test2 = list()
for key, val in time.items():
	tup = (key, val)
	test2.append(tup)

test2.sort()

for key, val in test2:
	print key, val



