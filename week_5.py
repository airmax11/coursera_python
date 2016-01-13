'''
9.4 Write a program to read through the mbox-short.txt and figure out who has
 the sent the greatest number of mail messages. The program looks for 'From ' 
 lines and takes the second word of those lines as the person who sent the mail.
  The program creates a Python dictionary that maps the sender's mail address to 
  a count of the number of times they appear in the file. After the dictionary 
  is produced, the program reads through the dictionary using a maximum loop to 
  find the most prolific committer.
'''

read_file = raw_input('Enter file name:')

if len(read_file) < 1:
	read_file = 'mbox-short.txt'

opfl = open(read_file)


lst = list()

for i in opfl:
	if i.startswith("From "):
		temp = i.split()
		lst.append(temp[1])

dct = dict()

for t in lst:
	dct[t] = dct.get(t, 0) + 1


maxkee = None
maxval = None

for kee, val in dct.items():
	if maxval == None or maxval < val:
		maxkee = kee
		maxval = val 


print maxkee, maxval




