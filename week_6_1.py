# week_6

import json
import urllib

enter_url = raw_input ("Enter your URL or use 1 for Sample and 2 for Actual problem. ")

if enter_url == '1':
	enter_url =  'http://python-data.dr-chuck.net/comments_42.json'
if enter_url == '2':
	enter_url = "http://python-data.dr-chuck.net/comments_174938.json"


open_url = urllib.urlopen(enter_url).read()





to_json = json.loads(open_url)

tlist = to_json["comments"]

count = 0
summa = 0

for i in tlist:
	count = count + 1
	summa = summa + int(i['count'])


print "Count = ", count
print "Sum = ", summa

