import face_recognition
import urllib.request
import boto3
import requests
import pyodbc
from time import time
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from PIL import Image, ImageDraw
import io,base64
import numpy as np

from io import BytesIO, StringIO

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

cors = CORS(app)

conn = pyodbc.connect(
    # Driver que será utilizado na conexão
    'DRIVER={ODBC Driver 17 for SQL Server};'
    # IP ou nome do servidor.
    'SERVER=gonder.c76jyhbi90dm.sa-east-1.rds.amazonaws.com;'
    # Porta
    'PORT=1433;'
    # Banco que será utilizado.
    'DATABASE=Api;'
    # Nome de usuário.
    f'UID=gonder;'
    # Senha.
    f'PWD=G0nder!#200&')  # integrated security

cursor = conn.cursor()


@app.route('/teste', methods=['POST'])
def teste():
    req_data = request.get_json(force=True)

    token = req_data['token']
    if(token != 'df9e299a3f37269c51626c9440c94372'):

        result = {
                   "status": False,
                   "message": 'Token inválido',
                 }
        return jsonify(result)

    else:

        client_id = req_data['client_id']

        SQL = ('''

SELECT 
       [encoding1]
      ,[encoding2]
      ,[encoding3]
      ,[encoding4]
      ,[encoding5]
      ,[encoding6]
      ,[encoding7]
      ,[encoding8]
      ,[encoding9]
      ,[encoding10]
      ,[encoding11]
      ,[encoding12]
      ,[encoding13]
      ,[encoding14]
      ,[encoding15]
      ,[encoding16]
      ,[encoding17]
      ,[encoding18]
      ,[encoding19]
      ,[encoding20]
      ,[encoding21]
      ,[encoding22]
      ,[encoding23]
      ,[encoding24]
      ,[encoding25]
      ,[encoding26]
      ,[encoding27]
      ,[encoding28]
      ,[encoding29]
      ,[encoding30]
      ,[encoding31]
      ,[encoding32]
      ,[encoding33]
      ,[encoding34]
      ,[encoding35]
      ,[encoding36]
      ,[encoding37]
      ,[encoding38]
      ,[encoding39]
      ,[encoding40]
      ,[encoding41]
      ,[encoding42]
      ,[encoding43]
      ,[encoding44]
      ,[encoding45]
      ,[encoding46]
      ,[encoding47]
      ,[encoding48]
      ,[encoding49]
      ,[encoding50]
      ,[encoding51]
      ,[encoding52]
      ,[encoding53]
      ,[encoding54]
      ,[encoding55]
      ,[encoding56]
      ,[encoding57]
      ,[encoding58]
      ,[encoding59]
      ,[encoding60]
      ,[encoding61]
      ,[encoding62]
      ,[encoding63]
      ,[encoding64]
      ,[encoding65]
      ,[encoding66]
      ,[encoding67]
      ,[encoding68]
      ,[encoding69]
      ,[encoding70]
      ,[encoding71]
      ,[encoding72]
      ,[encoding73]
      ,[encoding74]
      ,[encoding75]
      ,[encoding76]
      ,[encoding77]
      ,[encoding78]
      ,[encoding79]
      ,[encoding80]
      ,[encoding81]
      ,[encoding82]
      ,[encoding83]
      ,[encoding84]
      ,[encoding85]
      ,[encoding86]
      ,[encoding87]
      ,[encoding88]
      ,[encoding89]
      ,[encoding90]
      ,[encoding91]
      ,[encoding92]
      ,[encoding93]
      ,[encoding94]
      ,[encoding95]
      ,[encoding96]
      ,[encoding97]
      ,[encoding98]
      ,[encoding99]
      ,[encoding100]
      ,[encoding101]
      ,[encoding102]
      ,[encoding103]
      ,[encoding104]
      ,[encoding105]
      ,[encoding106]
      ,[encoding107]
      ,[encoding108]
      ,[encoding109]
      ,[encoding110]
      ,[encoding111]
      ,[encoding112]
      ,[encoding113]
      ,[encoding114]
      ,[encoding115]
      ,[encoding116]
      ,[encoding117]
      ,[encoding118]
      ,[encoding119]
      ,[encoding120]
      ,[encoding121]
      ,[encoding122]
      ,[encoding123]
      ,[encoding124]
      ,[encoding125]
      ,[encoding126]
      ,[encoding127]
      ,[encoding128]
  FROM [dbo].[face_encodings]
        ''')
        cursor = conn.cursor()
        cursor.execute(SQL)
        row = cursor.fetchall()
        starttime = time()
    
        data = []
        for r in row:

            base64String = req_data['imageData']

            unkown_image = face_recognition.load_image_file(io.BytesIO(base64.b64decode(base64String)))

            unkown_face_encoding = face_recognition.face_encodings(unkown_image)[0]

            data.append(r)


    return format(data), 200

  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
