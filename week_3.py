# test
#print ('hello Max!')


fname = raw_input ('Enter your file name or push Enter button :')

if len(fname) == 0:
	fname = 'words.txt'

try:
	file_open = open(fname)
except:
	print ('Incorrect file name. End of session.')
	exit()

for line in file_open:
	print line.rstrip().upper()