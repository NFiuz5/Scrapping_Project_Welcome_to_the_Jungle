import requests as req
from bs4 import BeautifulSoup
import time
import json

url = 'http://www.useragentstring.com/pages/useragentstring.php?name=Firefox'
save_list = []
def save(ua):
  save_list.append(ua)

def getUa(br):

  url = 'http://www.useragentstring.com/pages/useragentstring.php?name='+br
  r = req.get(url)

  if r.status_code == 200:
    soup = BeautifulSoup(r.content,'html.parser')
  else:
    soup = False

  if soup:
    div = soup.find('div',{'id':'liste'})
    lnk = div.findAll('a')

    for i in lnk:
      try:
        save(i.text)
      except:
        print('no ua')
  else:
    print('No soup for '+br)



lst = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']

for i in lst:
  getUa(i)
  file = f"C:/Users/hippo/Desktop/Scraping/files/User agents/{i}.json"

  with open(file,'a') as f:
    json.dump(save_list, f, indent=4)

  time.sleep(20)
  save_list = []
