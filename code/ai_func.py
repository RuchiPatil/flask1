import urllib.request
import face_recognition
import json
import cv2
import os
from gen_func import *
'''
AI Module : Functions that perform detection and recognition; are
called by the scheduler
'''

# ----------------------------------------------------- WRITE ENCODINGS
def write_encodings(newNames):
    known_face_encodings = []
    known_face_names = []

    # someones_face = face_recognition.load_image_file()

    for x in range(0, len(newNames)):
        reco_image = face_recognition.load_image_file(f"./images/{newNames[x]}.jpg")
        face_encoding = face_recognition.face_encodings(reco_image)[0]

        # add check here to make sure there are faces in the image
        all_face_locations = face_recognition.face_locations(reco_image, model="hog")
        print(f'num of faces : {len(all_face_locations)}')
        if len(all_face_locations) < 1:
            raise Exception("no faces in new-member pic")
        #save face encoding in json: users.json
        jsonFile = 'USERS/users.json'
        writeToJson(jsonFile, newNames[x], face_encoding)
    return 'Wrote to users.json'
# ----------------------------------------------------- GET ENCODINGS
def get_encodings():
    known_face_names = []
    known_face_encodings = []

    with open('USERS/users.json', 'r') as file:
        enc_data = json.load(file)

    for x in range(0, len(enc_data)):
        known_face_names.append(enc_data[x]["first_name"]) #save all fnames
        known_face_encodings.append(enc_data[x]["enc"]) #save all encodings

    return known_face_encodings, known_face_names

# ------------------------------------------------------- COMPARE DETECTECTED
def compare_faces(site_cap_image):

    face_enc, name_enc = get_encodings()
    #print(f"face_encodings: {face_enc}")
    #site_cap_image = 'site_photo.jpg'
    cv_site_cap_image = cv2.imread(site_cap_image)
    image_to_reco = face_recognition.load_image_file(site_cap_image)
    all_face_locations = face_recognition.face_locations(image_to_reco, model="hog")
    all_face_encodings = face_recognition.face_encodings(image_to_reco, all_face_locations)
    faces_found = []

    print("{} faces found in total.".format(len(all_face_locations)))
    for current_face_location, current_face_encoding in zip(all_face_locations, all_face_encodings):
        # split the tuple
        t_p, r_p, b_p, l_p = current_face_location

        # compare for face matches (based on known faces)
        # current_face_encodings refers to test image, known_face_enc refers to training images
        all_matches = face_recognition.compare_faces(face_enc, current_face_encoding)

        # init an unknown name string
        person_name = "Unknown"

        # if match found, use first kind of name
        if True in all_matches:
            first_match_index = all_matches.index(True)
            person_name = name_enc[first_match_index]
        faces_found.append(person_name)

            # visual label
        cv2.rectangle(cv_site_cap_image, (l_p, t_p), (r_p, b_p), (255, 0, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(cv_site_cap_image, person_name, (l_p, b_p), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Identified', cv_site_cap_image)

    return faces_found





#eof
