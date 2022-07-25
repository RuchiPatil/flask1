from flask import Flask, request, Response, send_file, send_from_directory
import numpy as np
import cv2
from firebase import find_new_faces
from ai_func import write_encodings, compare
from gen_func import doorImage
# Initialize the Flask application
app = Flask(__name__)

new_name = 'stst'
# route http posts to this method

#RIGHT NOW WE ARE USING ZUKO PRINT TO ADD NEW MEMBERS - change name of function and TELL VIKTOR
@app.route('/zuko_print', methods=['POST'])
def zuko_print():
    newNames = find_new_faces()
    #now add new new names to known encodings
    write_encodings(newNames)


#UPON REQUEST sending image to Receiver (and then deleteing image 1 minute after sending)
@app.route("/old_download_image")
def old_download_image():
    send_from_directory('./', f"{new_name}.jpg", as_attachment=True)
    return Response(response=new_name, mimetype="text")
    #return send_file(img, mimetype='image/gif', as_attachment=True)



#UPON REQUEST receiving image from Sender
#send to client
@app.route("/get_image", methods=['GET'])
def get_image():
    imgToComp = doorImage(request)
    faces_found =compare_faces(imgToComp)
    print(faces_found)










# start flask app
app.run(host="0.0.0.0", port=80)
