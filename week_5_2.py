'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
 the sent the greatest number of mail messages. The program looks for 'From ' 
 lines and takes the second word of those lines as the person who sent the mail.
  The program creates a Python dictionary that maps the sender's mail address to 
  a count of the number of times they appear in the file. After the dictionary 
  is produced, the program reads through the dictionary using a maximum loop to 
  find the most prolific committer.
'''

rf = raw_input ('File name txt:')

if len(rf) < 1:
	rf = 'mbox-short.txt'

flop = open (rf)

lst = list()

for i in flop:
	if i.startswith('From '):
		temp = i.split()
		lst.append(temp[1])



dct = dict()

for i in lst:
	dct[i] = dct.get(i, 0) + 1

maxkee = None
maxval = None

for kee, val in dct.items():
	if maxval == None or maxval < val:
		maxval = val
		maxkee = kee
	
print maxkee, maxval


