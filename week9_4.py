name = raw_input("Enter file:")

if len(name) < 1 :
	 name = "mbox-short.txt"
handle = open(name)

cou = dict()




for line in handle:
	    test = line.split()
	    if len(test) < 2 : continue
	    if test[0] != "From" : continue
	    mail = test[1]
	    cou[mail] = cou.get(mail,0) + 1



bigcount = None
bigname = None

for name,count in cou.items():
	if bigname is None or count > bigcount:
		bigname = name
		bigcount = count
print bigname, bigcount