import random
import json
import urllib.request




def bagitems():
  randlist = [random.randint(1,2000) for i in range(5) ]
  bag = []
  for i in randlist:
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    bag.append(result["objectName"])
  
  
  return bag