import json
import urllib


enter_url = raw_input ("Your URL adress or 1 for use your API or 2 for GOOGLE API: ")

#if len(enter_url) < 1 : break

if enter_url == '1':
	enter_url = 'http://python-data.dr-chuck.net/geojson?'

if enter_url =='2':
	enter_url = 'http://maps.googleapis.com/maps/api/geocode/json?'



address = raw_input ("Enter your location :")
#if len (adress) < 1 : break

url = enter_url + urllib.urlencode({'sensor':'false', 'address': address})
print url

url_open = urllib.urlopen (url).read()

js = json.loads(str(url_open))

print json.dumps(js, indent = 4)

location = js['results'][0]['place_id']
location2 = js['results'][0]['formatted_address']

print location
print location2