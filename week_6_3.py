 import json
 import urllib


 enter_url = raw_input ("Your URL adress or 1 for use your API : ")


 if len (enter_url) < 1:
 	break

 elif enter_url == '1':
 	enter_url = 'http://python-data.dr-chuck.net/geojson'



 adress = raw_input ("Enter your location :")
 if len (adress) < 1 :
 	break

 url = enter_url + urllib.urlencode({'sensor':'false', 'address': address})

 print url