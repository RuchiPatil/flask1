from flask import Flask, request, Response, send_file, send_from_directory
import numpy as np
import cv2
from fire_func import find_new_faces
from ai_func import *
from gen_func import *
# Initialize the Flask application
app = Flask(__name__)

new_name = 'stst' #do we need this? used in old_download_image
# route http posts to this method

#RIGHT NOW WE ARE USING ZUKO PRINT TO ADD NEW MEMBERS - change name of function and TELL VIKTOR
@app.route('/zuko_print', methods=['POST'])
def zuko_print():
    newNames = find_new_faces() #add new-member images to /images and new-members to users.json
    #now add new new names to known encodings
    write_encodings(newNames)
    ''' ok so in find_new_faces, another read for unlocking module
    then, add to encoding json (also do we need just users.json?)
    '''


#UPON REQUEST sending image to Receiver (and then deleteing image 1 minute after sending)
@app.route("/old_download_image")
def old_download_image():
    send_from_directory('./', f"{new_name}.jpg", as_attachment=True)
    return Response(response=new_name, mimetype="text")
    #return send_file(img, mimetype='image/gif', as_attachment=True)
# ---------- are we even using this function ^ ?


#UPON REQUEST receiving image from Sender
#send to client
@app.route("/get_image", methods=['GET', 'POST'])
def get_image():
    imgToComp = getDoorImage(request, "who.jpg")
    faces_found = compare_faces(imgToComp)
    '''
    send EMAIL/SMS
    '''
    #print(faces_found)
    '''
    if faces_found[i]['unlocking'] = 'yes' (in users_enc.json), then
    write yes/no  to lock.text
     '''
    toUnlock = f"NO or YES and person is {faces_found.toString()}"
    delete("who.jpg")
    return Response(response="toUnlock", status=200, mimetype="text/xml")










# start flask app
app.run(host="0.0.0.0", port=80)
