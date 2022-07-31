from flask import Flask, request, Response, send_file, send_from_directory
import json
import numpy as np
import cv2
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def getDoorImage(r, doorimg):

    #get image from client
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(doorimg, img)
    print("boom")

    '''
    # ESP-VERSION
    webserver_path = 'http://192.168.2.120/saved-photo'
    captured_image = 'site_photo.jpg'
    # This line grabs the image from the webserver and saves in CWD as 'site_photo.jpg'
    urllib.request.urlretrieve(webserver_path, captured_image)
    #EOF ESP-VERSION

    # _________________________________ MOCK VERSION
    mock_url = 'http://127.0.0.1:81'
    urllib.request.urlretrieve(mock_url)
    if len(glob.glob('../../../downloads/pic.jpg')) > 0:
        print("pic found in downloads")
        shutil.move('../../../downloads/pic.jpg', './')
    else:
        print(f"waht {glob.glob('../../../downloads/pic.jpg')}")
    # __________________________________ EOF MOCK VERSION
    '''
def sendEmail(faces_found):

    message = Mail(
        from_email='theverycleverbell@gmail.com',
        to_emails='ruchipatil@outlook.com, viktor.vcz88@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content=f'<strong>faces found: {faces_found}</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

def deleteImage(img):
    os.remove(img)

def writeToTxt(file, data):
    txt = open(file, "w")
    txt.write(data)
    txt.close()

def readFromTxt(file):
    txt = open(file, "r")
    data = txt.read()
    txt.close()
    return data

def clearTxt(file):
    txt = open(file, "w")
    txt.close()

def writeToJson(jsonFile, newName, face_encoding):
    newObj = []
    if os.path.isfile(jsonFile) is False:
        raise Exception("/USERS/users.json File NOT found.")

    with open(jsonFile) as fp:
        newObj = json.load(fp)
    enc = face_encoding.tolist()

    newObj.append({
    "first_name": newName,
    "enc": enc
    })

    with open(jsonFile, 'w') as json_file:
        json.dump(newObj, json_file, indent=4, separators=(',', ': '))












#eof
