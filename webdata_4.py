

import urllib 
from BeautifulSoup import *


url = raw_input ("Enter url  or use 1 for Sample Problem, 2 for Actual Problem:")
position = (int(raw_input("Enter position of URL :"))) - 1
count = (int(raw_input("Enter count of execution :"))) - 1

if url == '1':
	url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
if url == '2':
	url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Zahira.html'



html = urllib.urlopen(url).read()
soap = BeautifulSoup(html)


tags = soap('a')

listwithUrls = list()
print "Retrieving :" + url
for i in tags:
	temp = i.get('href', None)
	
	listwithUrls.append(temp)



for  t in range(count):

	urlfromlist = urllib.urlopen(listwithUrls[position])
	print "Retrieving :" + listwithUrls[position]
	del listwithUrls[:]
	
	soap2 = BeautifulSoup(urlfromlist)
	tags2 = soap2('a')
	for i in tags2:
		temp2 = i.get('href', None)

		
		listwithUrls.append(temp2)


print "Last URL is :" + listwithUrls[position]






#print listwithUrls
