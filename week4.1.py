## Week 4 . 1

inp = raw_input("Enter file name or press Enter button:")

if inp == '':
	inp = 'romeo.txt'

file_open = open(inp)

lst = list()
for i in file_open:
	
	test = i.rstrip().split()

	for n in test:
		if n not in lst:
			lst.append(n)


lst.sort()

print lst

	

