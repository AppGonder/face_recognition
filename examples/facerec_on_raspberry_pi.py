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
import requests
import pyodbc

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")

SQL = "selecT aws_tag as aws_key, name as name, registration as registration from operators where client_id = '1' and file_name <> '' and id = 38"
cursor = conn.cursor()
cursor.execute(SQL)
row = cursor.fetchall()

# Loop through each person in the training directory
for r in row:

    s3 = boto3.client('s3')
    # Generate the URL to get 'key-name' from 'bucket-name'
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'siftmov',
            'Key': 'operadores/' + r.aws_key
        }
    )
    response = urllib.request.urlopen(url)

    # Get the face encodings for the face in each image file
    face = face_recognition.load_image_file(response)
    face_bounding_boxes = face_recognition.face_locations(face)

    kwown_face_encoding = face_recognition.face_encodings(face)[0]

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
        face_encodings = face_recognition.face_encodings(output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([kwown_face_encoding], face_encoding)
            name = "<Unknown Person>"

            if match[0]:
                name = r.name

            print("I see someone named {}!".format(name))
