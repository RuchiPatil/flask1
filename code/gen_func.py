from flask import Flask, request, Response, send_file, send_from_directory

import numpy as np
import cv2

def doorImage(r):
    '''
    # ESP-VERSION
    webserver_path = 'http://192.168.2.120/saved-photo'
    captured_image = 'site_photo.jpg'
    # This line grabs the image from the webserver and saves in CWD as 'site_photo.jpg'
    urllib.request.urlretrieve(webserver_path, captured_image)
    #EOF ESP-VERSION
    '''
    # _________________________________ MOCK VERSION
    mock_url = 'http://127.0.0.1:81'
    urllib.request.urlretrieve(mock_url)
    if len(glob.glob('../../../downloads/pic.jpg')) > 0:
        print("pic found in downloads")
        shutil.move('../../../downloads/pic.jpg', './')
    else:
        print(f"waht {glob.glob('../../../downloads/pic.jpg')}")
    # __________________________________ EOF MOCK VERSION
