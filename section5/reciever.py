from __future__ import print_function
import requests
import json
import cv2
from datetime import datetime
import numpy as np
import base64
#import urllib.request
from urllib.request import urlretrieve


addr = 'http://127.0.0.1:5000'
ext = '/lol_idk'
get_url = addr + ext

currtime = datetime.now()
imgname = currtime.strftime("%H%M%S.jpg")

#urlretrieve(get_url, imgname)

#prepare headers for http request
content_type = 'text'
headers = {'content-type': content_type}

#person_name = requests.get(get_url, stream=True)
response = requests.get(get_url)
data = response.json()
#print(json.loads(response.text))
print(data["name"])
name = data["name"]
img_encoded = data["img"]["py/b64"]
img_encoded = base64.b64decode(img_encoded)

print(img_encoded)
#print(f"IMAGE STUFF : \n{img_encoded}\n")
nparr = np.frombuffer(img_encoded, np.uint8)
# decode image
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
cv2.imwrite("boingboing.jpg", img)

#print(person_name)
'''
r = requests.get(get_url)
nparr = np.fromstring(r, np.uint8)
# decode image
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
cv2.imwrite(f"{name}.jpg", img)

response = requests.post(get_url, headers=headers)
r = response #json.loads(response.text)
print(f"RESPONSE IS  {r}  u got itttt?\n\n")


currtime = datetime.now()
imgname = currtime.strftime("%H%M%S")

#img_json = json.loads(r.text)
img = cv2.imdecode(r, cv2.IMREAD_COLOR)
cv2.imwrite(imgname, img)

# decode response
print(r.text)
'''
