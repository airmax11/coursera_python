import  urllib 
from BeautifulSoup import *

#link position, will be modified tpr times #lp = 3
lp = 18
#times the process is repeated #tpr = 4
tpr = 7
# url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html' url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Madilyn.html'
for i in range(tpr):
	url = BeautifulSoup(urllib.request.urlopen(url).read())('a')[lp - 1].get('href', None) 
	print(url)