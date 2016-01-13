'''
7.2 Write a program that prompts for a file name, then opens that 
file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values 
from each of the lines and compute the average of those values and produce an output as shown below.
You can download the sample data at 
http://www.pythonlearn.com/code/mbox-short.txt when you are
 testing below enter mbox-short.txt as the file name.
'''

file_name = raw_input ('Enter file name or press enter button :')

if len (file_name) == 0: 
	file_name = 'mbox-short.txt'

try:
	file_open = open(file_name)

except:
	'Incorrect file name.'
	exit()

count = 0
value = 0
for line in file_open:
	if line.startswith('X-DSPAM-Confidence:'):
		##sel_val = line[28:]
		#print sel_val
		select_value = float(line[(len('X-DSPAM-Confidence: ')) :].rstrip())
		value = value + select_value
		count = count + 1
		continue

print 'Average spam confidence:', value/count



