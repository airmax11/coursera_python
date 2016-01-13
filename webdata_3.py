# week 6


import urllib
from BeautifulSoup import *


url = raw_input("Enter your url :")

if len(url)<1:
	url= 'http://python-data.dr-chuck.net/comments_174937.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

count = 0
summa = 0

for tag in tags:
	temp = tag.contents[0]
	summa = summa + int(temp)
	count += 1

print count, summa
