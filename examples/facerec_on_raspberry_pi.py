# This is a demo of running face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes to the console.

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.
# You can follow this installation instructions to get your RPi set up:
# https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

import face_recognition
import picamera
import numpy as np
import face_recognition
import urllib.request
import boto3
import json
import requests

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Initialize some variables
face_locations = []
face_encodings = []

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_enc = face_recognition.face_encodings(output, face_locations)[0]

    if(len(face_locations) > 0):

        data = { 'face_enc0':face_enc[0], 'face_enc1':face_enc[1], 'face_enc2':face_enc[2], 'face_enc3': face_enc[3], 'face_enc4': face_enc[4], 'face_enc5': face_enc[5],
            'face_enc6':face_enc[6], 'face_enc7':face_enc[7], 'face_enc8':face_enc[8],'face_enc9':face_enc[9], 'face_enc10':face_enc[10], 'face_enc11':face_enc[11],
            'face_enc12':face_enc[12], 'face_enc13':face_enc[13], 'face_enc14':face_enc[14], 'face_enc15':face_enc[15], 'face_enc16':face_enc[16], 'face_enc17':face_enc[17],
            'face_enc18':face_enc[18], 'face_enc19':face_enc[19],'face_enc20':face_enc[20], 'face_enc21':face_enc[21], 'face_enc22':face_enc[22], 'face_enc23':face_enc[23],
            'face_enc24':face_enc[24], 'face_enc25':face_enc[25], 'face_enc26':face_enc[26], 'face_enc27':face_enc[27], 'face_enc28':face_enc[28], 'face_enc29':face_enc[29],
            'face_enc30':face_enc[30], 'face_enc31':face_enc[31], 'face_enc32':face_enc[32], 'face_enc33':face_enc[33], 'face_enc34':face_enc[34], 'face_enc35':face_enc[35],
            'face_enc36':face_enc[36], 'face_enc37':face_enc[37], 'face_enc38':face_enc[38], 'face_enc39':face_enc[39], 'face_enc40':face_enc[40], 'face_enc41':face_enc[41],
            'face_enc42':face_enc[42], 'face_enc43':face_enc[43], 'face_enc44':face_enc[44], 'face_enc45':face_enc[45], 'face_enc46':face_enc[46], 'face_enc47':face_enc[47],
            'face_enc48':face_enc[48], 'face_enc49':face_enc[49], 'face_enc50':face_enc[50], 'face_enc51':face_enc[51], 'face_enc52':face_enc[52], 'face_enc53':face_enc[53],
            'face_enc54':face_enc[54], 'face_enc55':face_enc[55], 'face_enc56':face_enc[56], 'face_enc57':face_enc[57], 'face_enc58':face_enc[58], 'face_enc59':face_enc[59],
            'face_enc60':face_enc[60], 'face_enc61':face_enc[61], 'face_enc62':face_enc[62], 'face_enc63':face_enc[63], 'face_enc64':face_enc[64], 'face_enc65':face_enc[65],
            'face_enc66':face_enc[66], 'face_enc67':face_enc[67], 'face_enc68':face_enc[68], 'face_enc69':face_enc[69], 'face_enc70':face_enc[70], 'face_enc71':face_enc[71],
            'face_enc72':face_enc[72], 'face_enc73':face_enc[73], 'face_enc74':face_enc[74], 'face_enc75':face_enc[75], 'face_enc76':face_enc[76], 'face_enc77':face_enc[77],
            'face_enc78':face_enc[78], 'face_enc79':face_enc[79], 'face_enc80':face_enc[80], 'face_enc81':face_enc[81], 'face_enc82':face_enc[82], 'face_enc83':face_enc[83],
            'face_enc84':face_enc[84], 'face_enc85':face_enc[85], 'face_enc86':face_enc[86], 'face_enc87':face_enc[87], 'face_enc88':face_enc[88], 'face_enc89':face_enc[89],
            'face_enc90':face_enc[90], 'face_enc91':face_enc[91], 'face_enc92':face_enc[92], 'face_enc93':face_enc[93], 'face_enc94':face_enc[94], 'face_enc95':face_enc[95],
            'face_enc96':face_enc[96], 'face_enc97':face_enc[97], 'face_enc98':face_enc[98], 'face_enc99':face_enc[99], 'face_enc100':face_enc[100], 'face_enc101':face_enc[101],
            'face_enc102':face_enc[102], 'face_enc103':face_enc[103], 'face_enc104':face_enc[104], 'face_enc105':face_enc[105], 'face_enc106':face_enc[106], 'face_enc107':face_enc[107],
            'face_enc108':face_enc[108], 'face_enc109':face_enc[109], 'face_enc110':face_enc[110], 'face_enc111':face_enc[111], 'face_enc112':face_enc[112], 'face_enc113':face_enc[113],
            'face_enc114':face_enc[114], 'face_enc115':face_enc[115], 'face_enc116':face_enc[116], 'face_enc117':face_enc[117], 'face_enc118':face_enc[118], 'face_enc119':face_enc[119], 
            'face_enc120':face_enc[120], 'face_enc121':face_enc[121], 'face_enc122':face_enc[122], 'face_enc123':face_enc[123], 'face_enc124':face_enc[124], 'face_enc125':face_enc[125],
            'face_enc126':face_enc[126], 'face_enc127':face_enc[127]}

        API_ENDPOINT = "https://api.siftmov.com.br/api/raspberry/df9e299a3f37269c51626c9440c94372"

        response = requests.post(url = API_ENDPOINT, data = data)
            
        result = response.text

        if len(result) > 0:

            print("I see someone named: {}!".format(result))

        else:
            print("<Unknown Person>")

