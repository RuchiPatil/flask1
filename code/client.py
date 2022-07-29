from __future__ import print_function
import requests
import json
import cv2

addr = 'http://68.183.201.80:5000'
test_url = addr + '/get_image'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('tina.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)

# send http request with image and receive response
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)

'''headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
datasend = {"message" : "hallllloo"}
response = requests.post(test_url, data=datasend, headers=headers)'''
# decode response
print(json.loads(response.text))

# expected output: {u'message': u'image received. size=124x124'}
