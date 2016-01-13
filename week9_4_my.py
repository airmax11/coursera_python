file_name = raw_input ("Enter file name:")

if len(file_name) < 1:
	file_name = 'mbox-short.txt'


try:
	open_file = open (file_name)

except:
	print "Can't open the file."


list_with_emails = []


for line in open_file:
	if line.startswith("From: "):
		line.rstrip()
		variab = line.split()
		list_with_emails.append(variab[1])
		

dic = {}

for item in list_with_emails:
	dic[item] = dic.get(item, 0) + 1


maxcount = None
maxemail = None

for key, value in dic.items():
	if maxcount == None or maxcount < value:
		maxcount = value
		maxemail = key





print maxemail, maxcount

