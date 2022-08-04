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
    print("linda/blom")

def sendSMS(faces_found):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')

    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    #Change the value of 'from' with the number
    #received from Twilio and the value of 'to'
    #with the number in which you want to send message.
    numbers = ['+16473909082', '+15197744393', '+16475289062']
    for number in numbers:
        message = client.messages.create(
                                      from_='+19382225448',
                                      body =faces_found,
                                      to = number
                                  )

        print(message.sid)
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
#sendEmail(["hfkajshljskahfls"])









#eof
