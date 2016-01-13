#regex
import re

file_name = raw_input ("Enter file name: ")

if len(file_name) < 1:
	file_name = 're01.txt'

file_open = open (file_name)

value = 0

for i in file_open:
	text = re.findall('[0-9]+', i)
	for a in text:
		if len(a) > 0:
			value = value + int(a)



print value
print "Done"

			