#web_data1.py

import urllib

openurl = urllib.urlopen ("http://www.pythonlearn.com/code/intro-short.txt")


temp = openurl.read()

test = dict()

for i in temp:

	
	test[i] = test.get(i, 0) + 1


print test

