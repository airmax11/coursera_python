#week Extracting Data from XML

import urllib
import xml.etree.ElementTree as ET
import re


url = raw_input ("Enter your url or 1 fro Sample, 2 for Actual :" )

if url == '1':
	url = 'http://python-data.dr-chuck.net/comments_42.xml'

if url == '2':
	url = 'http://python-data.dr-chuck.net/comments_174934.xml'



page = urllib.urlopen(url)
data  = page.read()
print "Total characters :", len(data)
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

print "Count :", len(lst)

total_sum = 0

for i in lst:

	value = int(i.find('count').text)

	total_sum += value

print "Sum = ",total_sum

'''
--Alternative--
counts = tree.findall('.//count')
for i in counts:
	print i.text
'''