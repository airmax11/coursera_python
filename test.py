#test.py
import string

file_name = raw_input ("Your file name:")

if file_name == "":

	file_name = "test.txt"

print file_name
try:
	open_file = open (file_name)

except:
	print "Can't open the file."

new_text = open_file.read()
new_text.rstrip()
new_list = new_text.split()

"""
for line in new_text:
	line = line.translate (None, string.punctuation )
	line = line.lower()
	"""


counts = {}


for words in new_list:
	counts[words] = counts.get(words, 0) + 1



bigcount = None 
bigword = None

for key, value in counts.items():
	if bigcount == None or value > bigcount:
		bigcount = value
		bigword = key

print counts
print "----------------------"
print bigword, bigcount

