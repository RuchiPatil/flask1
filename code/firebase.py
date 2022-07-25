import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from datetime import timedelta
import urllib
import json
import os

# VARIABLES USED --------------------------------------------------------------------------------------------
cred = credentials.Certificate("./fire/key.json")
app = firebase_admin.initialize_app(cred, {"storageBucket" : 'cappstone-fcf0f.appspot.com'}, name='storage')

config = {
  "apiKey": "AIzaSyDaPLo76eJGXJaF6pzg3UHspIXgQ8bs3PA",
  "authDomain": "cappstone-fcf0f.firebaseapp.com",
  "databaseURL": "https://cappstone-fcf0f-default-rtdb.firebaseio.com",
  "projectId": "cappstone-fcf0f",
  "storageBucket": "cappstone-fcf0f.appspot.com",
  "messagingSenderId": "457263544867",
  "appId": "1:457263544867:web:0566601951f5a5a53b8f96",
  "measurementId": "G-VRRYSXR6VF"
};

def find_new_faces():
    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    # Read Data - list of names from firebase db
    fireNames = list(database.child("Posts").get().val())
    #print(fireNames)

    #List of names in users.json
    with open('USERS/users.json', 'r') as jsonFile:
        jsonData = json.load(jsonFile)
    jsonNames = [d['first_name'] for d in jsonData]
    #print(jsonNames)

    #LIST of new-member images (names) to download
    newNames = list(set(fireNames) - set(jsonNames))
    print(newNames)

    #download new member images, and save in images, and add to users.json
    for i in range(0, len(newNames)):
        #DONWLOAD IMAGE according to db comparison with user.json
        bucket = storage.bucket(app=app)
        blob = bucket.blob(f"images/{newNames[i]}.jpg")
        #print(blob.generate_signed_url(timedelta(seconds=300), method='GET'))
        #3999d5a4-fcdf-455a-954c-355deb3ae072
        urllib.request.urlretrieve(blob.generate_signed_url(timedelta(seconds=300), method='GET'), f"./images/{newNames[i]}.jpg")

        #add new-member to users.json
        jsonFile = 'USERS/users.json'
        newObj = []
        if os.path.isfile(jsonFile) is False:
            raise Exception("users.json File NOT found.")

        with open(jsonFile) as fp:
            newObj = json.load(fp)

        newObj.append({
        "first_name": newNames[i],
        "image": f"./images/{newNames[i]}.jpg",
        })

        with open(jsonFile, 'w') as json_file:
            json.dump(newObj, json_file, indent=4, separators=(',', ': '))
    return newNames
