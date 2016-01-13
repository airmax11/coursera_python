import json, urllib, urllib2, base64, time
 
## [readme]
#  (1). Install python 2.7 (this script will not work with python 3+)
#  (2). Install PushBullet to your mobile device's + set it up (takes few minutes)
#       - On PC, login to pushbullet.com and go to Account Settings, copy your API key and paste it into pushbullet_Key below
#  (3). Look at stores variable below to find the exact names of the stores you want to be checked, enter their names exactly as shown into allowedStores below (use a comma for multiple stores)
#       - DO NOT CHANGE stores/appleStores/appleStock URL's unless you know what you are doing / modfying this script for alternative locations (Canada?)
#  (4). Look at the models variable in the Vars section below, locate all of the model codes that you want to be notified of when they are in stock at the stores chosen
#       - Enter them into the wantedModels variable..
#  (5). Change nextCheck to how long to wait until performing the next check (this is in seconds, 60seconds is recommended!)
#  (6). Run script and leave running, as soon as there is stock for the chosen stores/models a PUSH notifation will be sent to all of your devices that are linked with the specified pushbullet account!
#
#
#  (*) - See below as an example of a configuration that checks the Basingstake/Southampton/Reading stores for ANY iPhone 6+ stock every 60seconds
## [/readme]
 
## Config
pushbullet_Key = "ujyIs6jfjvEsjAiVsKnSTs"
allowedStores = "Covent Garden, Regent Street"
wantedModels = {
                  # 6+ 16GB
                  "MGA92" : True,
                  "MGA82" : True,
                  "MGAA2" : True,
                  # 6+ 64GB
                  "MGAJ2" : True,
                  "MGAH2" : True,
                  "MGAK2" : True,
                  # 6+ 128GB
                  "MGAE2" : True,
                  "MGAC2" : True,
                  "MGAF2" : True
                };
nextCheck = 60
 
## Vars
appleStores = "https://reserve.cdn-apple.com/GB/en_GB/reserve/iPhone/stores.json"
appleStock = "https://reserve.cdn-apple.com/GB/en_GB/reserve/iPhone/availability.json"
stores = {
            "R227" : "Bentall Centre",
            "R113" : "Bluewater",
            "R340" : "Braehead",
            "R163" : "Brent Cross",
            "R496" : "Bromley",
            "R135" : "Buchanan Street",
            "R118" : "Bullring",
            "R252" : "Cabot Circus",
            "R391" : "Chapelfield",
            "R244" : "Churchill Square",
            "R245" : "Covent Garden",
            "R393" : "Cribbs Causeway",
            "R545" : "Drake Circus",
            "R341" : "Eldon Square",
            "R482" : "Festival Place",
            "R270" : "Grand Arcade",
            "R308" : "Highcross",
            "R242" : "Lakeside",
            "R239" : "Liverpool ONE",
            "R215" : "Manchester Arndale",
            "R153" : "Meadowhall",
            "R423" : "Metrocentre",
            "R269" : "Milton Keynes",
            "R279" : "Princesshay",
            "R092" : "Regent Street",
            "R335" : "SouthGate",
            "R334" : "St David's 2",
            "R410" : "Stratford City",
            "R176" : "The Oracle",
            "R255" : "Touchwood Centre",
            "R136" : "Trafford Centre",
            "R372" : "Trinity Leeds",
            "R363" : "Union Square",
            "R313" : "Victoria Square",
            "R527" : "Watford",
            "R174" : "WestQuay",
            "R226" : "White City",
            "R328" : "Princes Street"
         };
models = {  # iPhone 6
            "MG482" : "iPhone 6 Silver 16GB",           
            "MG472" : "iPhone 6 Space Gray 16GB",           
            "MG492" : "iPhone 6 Gold 16GB",
            "MG4H2" : "iPhone 6 Silver 64GB",           
            "MG4F2" : "iPhone 6 Space Gray 64GB",          
            "MG4J2" : "iPhone 6 Gold 64GB",
            "MG4C2" : "iPhone 6 Silver 128GB",           
            "MG4A2" : "iPhone 6 Space Gray 128GB",           
            "MG4E2" : "iPhone 6 Gold 128GB",
            # iPhone 6+
            "MGA92" : "iPhone 6+ Silver 16GB",
            "MGA82" : "iPhone 6+ Space Gray 16GB",    
            "MGAA2" : "iPhone 6+ Gold 16GB",
            "MGAJ2" : "iPhone 6+ Silver 64GB",           
            "MGAH2" : "iPhone 6+ Space Gray 64GB",  
            "MGAK2" : "iPhone 6+ Gold 64GB",
            "MGAE2" : "iPhone 6+ Silver 128GB",
            "MGAC2" : "iPhone 6+ Space Gray 128GB",
            "MGAF2" : "iPhone 6+ Gold 128GB"
          };
 
## Quick Classes
class AppleStore:
    def GetStores(self):
        storesData = urllib2.urlopen(appleStores).read()
        tmp = json.loads(storesData)
        tmp2 = {}
        for store in tmp['stores']:
            if store['storeEnabled']:
                tmp2[store['storeNumber']] = store['storeName']
         
        return tmp2
 
    def GetStock(self):
        return urllib2.urlopen(appleStock).read()
 
class PushBullet:
    def __init__(self, apiKey):
        self.key = apiKey
        self.auth = 'Basic {0}'.format(base64.b64encode(apiKey))
         
    def sendNote(self, title, message):
        header = { 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json', 'Authorization': self.auth }
        postData = urllib.urlencode({'type': 'note', 'title': title, 'body': message})
        req = urllib2.Request("https://api.pushbullet.com/v2/pushes", postData, header)
        return urllib2.urlopen(req).read()
         
 
## Funcs
def DoCheck():
    apple = AppleStore()
    push = PushBullet(pushbullet_Key)
 
    stock = apple.GetStock()
    tmp = json.loads(stock)
 
    for store in tmp:
        if store == "updated": continue
        if allowedStores.find(stores[store]) != -1:
            # Store is in allowedStores
            for item in tmp[store]:
                try:     # Exceptions will occour if model is not in the wanted list
                    if wantedModels[item[:5]] and tmp[store][item]:
                         # Found stock!
                        push.sendNote(models[item[:5]], "Stock found at " + stores[store] + "\n\n" + time.strftime('(%d.%b.%y/%I:%M%p)'))
                        print time.strftime('(%d.%b.%y/%I:%M%p)') + ": Found " + models[item[:5]] + " at " + stores[store]
                except:
                    pass # continue the loop as current model is not wanted
     
    print time.strftime('(%d.%b.%y/%I:%M%p)') + ": Finished checking..."
 
## Main Code
if __name__ == '__main__':
    #tmp = AppleStore()
    #stores = tmp.GetStores()
 
    while True:
        try:
            DoCheck()
        except:
            print time.strftime('(%d.%b.%y/%I:%M%p)') + ": Hmm, reserve for pickup may be down?"
 
        time.sleep(nextCheck)