#try to print only headers

def return_headers (file_name):

	file_open = open(file_name)
	
	lst = list()

	for i in file_open:
		test = i.rstrip().split('|')
		for t in test:
			if t not in lst:
				lst.append(t)

	lst.sort()

	for e in lst:
		print e



