

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for i in fh:

		test = i.rstrip().split()
		if len(test) < 1 : continue

		if test[0] == 'From':
			print test[1]
			count = count +1

		



print "There were", count, "lines in the file with From as the first word"

