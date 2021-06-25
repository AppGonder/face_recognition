import face_recognition
import urllib.request
import boto3
import requests
import pyodbc
from time import time
from flask import Flask, jsonify, request, redirect, g, render_template
from flask_cors import CORS
from PIL import Image, ImageDraw
import io
import time
import base64
import numpy as np
from datetime import datetime
import json
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


@app.route('/face-recognition', methods=['POST'])
def face():
    req_data = request.get_json(force=True)

    token = req_data['token']
    if(token != 'df9e299a3f37269c51626c9440c94372'):

        result = {
            "status": False,
            "message": 'Token inválido',
        }
        return jsonify(result)

    else:

        g.start = time.time()

        diff = str(round((time.time() - g.start) * 1000, 2)) + ' ms'

        client_id = req_data['client_id']

        base64String = req_data['imageData']

        unkown_image = face_recognition.load_image_file(io.BytesIO(base64.b64decode(base64String)))

        data = []

        face_found = False

        if(len(face_recognition.face_encodings(unkown_image)) > 0):

            face_enc = face_recognition.face_encodings(unkown_image)[0]

            SQL = ('''
            EXEC [Api].[dbo].[Face_Recognition]

            @client_id =?,
            @e1=?, @e2=?, @e3=?, @e4=?, @e5=?, @e6=?, @e7=?, @e8=?, @e9=?, @e10=?,
            @e11=?, @e12=?, @e13=?, @e14=?, @e15=?, @e16=?, @e17=?, @e18=?, @e19=?, @e20=?,
            @e21=?, @e22=?, @e23=?, @e24=?, @e25=?, @e26=?, @e27=?, @e28=?, @e29=?, @e30=?,
            @e31=?, @e32=?, @e33=?, @e34=?, @e35=?, @e36=?, @e37=?, @e38=?, @e39=?, @e40=?,
            @e41=?, @e42=?, @e43=?, @e44=?, @e45=?, @e46=?, @e47=?, @e48=?, @e49=?, @e50=?,
            @e51=?, @e52=?, @e53=?, @e54=?, @e55=?, @e56=?, @e57=?, @e58=?, @e59=?, @e60=?,
            @e61=?, @e62=?, @e63=?, @e64=?, @e65=?, @e66=?, @e67=?, @e68=?, @e69=?, @e70=?,
            @e71=?, @e72=?, @e73=?, @e74=?, @e75=?, @e76=?, @e77=?, @e78=?, @e79=?, @e80=?,
            @e81=?, @e82=?, @e83=?, @e84=?, @e85=?, @e86=?, @e87=?, @e88=?, @e89=?, @e90=?,
            @e91=?, @e92=?, @e93=?, @e94=?, @e95=?, @e96=?, @e97=?, @e98=?, @e99=?, @e100=?,
            @e101=?, @e102=?, @e103=?, @e104=?, @e105=?, @e106=?, @e107=?, @e108=?, @e109=?, @e110=?,
            @e111=?, @e112=?, @e113=?, @e114=?, @e115=?, @e116=?, @e117=?, @e118=?, @e119=?, @e120=?,
            @e121=?, @e122=?, @e123=?, @e124=?, @e125=?, @e126=?, @e127=?, @e128=?;

            ''')

            Values = [client_id, face_enc[0], face_enc[1], face_enc[2], face_enc[3], face_enc[4], face_enc[5], face_enc[6], face_enc[7], face_enc[8],
                    face_enc[9], face_enc[10], face_enc[11], face_enc[12], face_enc[13], face_enc[14], face_enc[15], face_enc[16], face_enc[17], face_enc[18], face_enc[19],
                    face_enc[20], face_enc[21], face_enc[22], face_enc[23], face_enc[24], face_enc[25], face_enc[26], face_enc[27], face_enc[28], face_enc[29], face_enc[30],
                    face_enc[31], face_enc[32], face_enc[33], face_enc[34], face_enc[35], face_enc[36], face_enc[37], face_enc[38], face_enc[39], face_enc[40], face_enc[41],
                    face_enc[42], face_enc[43], face_enc[44], face_enc[45], face_enc[46], face_enc[47], face_enc[48], face_enc[49], face_enc[50], face_enc[51], face_enc[52],
                    face_enc[53], face_enc[54], face_enc[55], face_enc[56], face_enc[57], face_enc[58], face_enc[59], face_enc[60], face_enc[61], face_enc[62], face_enc[63],
                    face_enc[64], face_enc[65], face_enc[66], face_enc[67], face_enc[68], face_enc[69], face_enc[70], face_enc[71], face_enc[72], face_enc[73], face_enc[74],
                    face_enc[75], face_enc[76], face_enc[77], face_enc[78], face_enc[79], face_enc[80], face_enc[81], face_enc[82], face_enc[83], face_enc[84], face_enc[85],
                    face_enc[86], face_enc[87], face_enc[88], face_enc[89], face_enc[90], face_enc[91], face_enc[92], face_enc[93], face_enc[94], face_enc[95], face_enc[96],
                    face_enc[97], face_enc[98], face_enc[99], face_enc[100], face_enc[101], face_enc[102], face_enc[103], face_enc[104], face_enc[105], face_enc[106], face_enc[107],
                    face_enc[108], face_enc[109], face_enc[110], face_enc[111], face_enc[112], face_enc[113], face_enc[114], face_enc[115], face_enc[116], face_enc[117], face_enc[118],
                    face_enc[119], face_enc[120], face_enc[121], face_enc[122], face_enc[123], face_enc[124], face_enc[125], face_enc[126], face_enc[127]]

            cursor = conn.cursor()
            cursor.execute(SQL, Values)
            row = cursor.fetchall()

            if len(row) > 0:

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
                    image = face_recognition.load_image_file(response)
                    face_locations = face_recognition.face_locations(image)
                    known_face_encoding = face_recognition.face_encodings(image)[0]

                    pil_image = Image.fromarray(image)

                    draw = ImageDraw.Draw(pil_image)

                    for (top, right, bottom, left), known_face_encoding in zip(face_locations, known_face_encoding):

                        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

                        name = [r.name][0]
                        text_width, text_height = draw.textsize(name)
                        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
                        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

                        del draw

                        im_file = BytesIO()
                        pil_image.save(im_file, format="JPEG")
                        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
                        im_b64 = base64.b64encode(im_bytes)

                        final = im_b64.decode('utf-8')

                        result = {
                            "face_found": True,
                            "name": r.name,
                            "registration": r.registration,
                            "request_time": diff,
                            "distance": r.distance,
                            "face_url": url,
                            "base64": 'data:image/jpeg;base64,' + format(final).replace("'", "")
                        }
                        data.append(result)

                        return jsonify(data), 200
            else:

                result = {
                    "face_found": False,
                    "request_time": diff
                }
                data.append(result)

            return jsonify(data), 200
        else:
            result = {
                    "face_found": False,
                    "request_time": diff
            }
            data.append(result)

        return jsonify(data), 200


@ app.route('/register-face-encodings', methods=['POST'])
def register():
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
        aws_id = req_data['aws_id']
        datetime = req_data['datetime']

        SQL = ('''
        selecT

        aws_tag as aws_id,
        name as name,
        operators.id as operator_id,
        registration as registration,
        ltrim(rtrim(isnull(operator_id,'insert'))) as face_encoded

        from operators

        left join face_encodings on
        face_encodings.client_id = operators.client_id and
        face_encodings.operator_id = operators.id

        where
        operators.client_id=? and file_name <> '' and aws_tag=?
        ''')
        Values = [client_id, aws_id]
        cursor = conn.cursor()
        cursor.execute(SQL, Values)

        row = cursor.fetchall()

        data = []

        for r in row:

            s3 = boto3.client('s3')
            # Generate the URL to get 'key-name' from 'bucket-name'
            url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': 'siftmov',
                    'Key': 'operadores/' + r.aws_id
                }
            )

            response = urllib.request.urlopen(url)

            # Get the face encodings for the face in each image file
            face = face_recognition.load_image_file(response)
            face_bounding_boxes = face_recognition.face_locations(face)

            face_enc = face_recognition.face_encodings(face)[0]

            if(r.face_encoded == 'insert'):

                SQLCommand = ('''
                INSERT INTO [dbo].[face_encodings]
                    ([client_id]
                    ,[created_at]
                    ,[updated_at]
                    ,[operator_id]
                    ,[encoding1]
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
                    ,[encoding128])
                VALUES
                    (?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?
                    ,?)
                    ''')
                Values = [client_id, datetime, '', r.operator_id, face_enc[0], face_enc[1], face_enc[2], face_enc[3], face_enc[4], face_enc[5], face_enc[6], face_enc[7], face_enc[8],
                        face_enc[9], face_enc[10], face_enc[11], face_enc[12], face_enc[13], face_enc[14], face_enc[15], face_enc[16], face_enc[17], face_enc[18], face_enc[19],
                        face_enc[20], face_enc[21], face_enc[22], face_enc[23], face_enc[24], face_enc[25], face_enc[26], face_enc[27], face_enc[28], face_enc[29], face_enc[30],
                        face_enc[31], face_enc[32], face_enc[33], face_enc[34], face_enc[35], face_enc[36], face_enc[37], face_enc[38], face_enc[39], face_enc[40], face_enc[41],
                        face_enc[42], face_enc[43], face_enc[44], face_enc[45], face_enc[46], face_enc[47], face_enc[48], face_enc[49], face_enc[50], face_enc[51], face_enc[52],
                        face_enc[53], face_enc[54], face_enc[55], face_enc[56], face_enc[57], face_enc[58], face_enc[59], face_enc[60], face_enc[61], face_enc[62], face_enc[63],
                        face_enc[64], face_enc[65], face_enc[66], face_enc[67], face_enc[68], face_enc[69], face_enc[70], face_enc[71], face_enc[72], face_enc[73], face_enc[74],
                        face_enc[75], face_enc[76], face_enc[77], face_enc[78], face_enc[79], face_enc[80], face_enc[81], face_enc[82], face_enc[83], face_enc[84], face_enc[85],
                        face_enc[86], face_enc[87], face_enc[88], face_enc[89], face_enc[90], face_enc[91], face_enc[92], face_enc[93], face_enc[94], face_enc[95], face_enc[96],
                        face_enc[97], face_enc[98], face_enc[99], face_enc[100], face_enc[101], face_enc[102], face_enc[103], face_enc[104], face_enc[105], face_enc[106], face_enc[107],
                        face_enc[108], face_enc[109], face_enc[110], face_enc[111], face_enc[112], face_enc[113], face_enc[114], face_enc[115], face_enc[116], face_enc[117], face_enc[118],
                        face_enc[119], face_enc[120], face_enc[121], face_enc[122], face_enc[123], face_enc[124], face_enc[125], face_enc[126], face_enc[127]]

                # Processing Query
                cursor.execute(SQLCommand, Values)

                conn.commit()

                result = {
                    "encoding": format(face_enc),
                    "status": True,
                    "action": 'insert'
                }
                data.append(result)
            
            else:

                SQLCommand = ('''
                    UPDATE [dbo].[face_encodings]
                    SET [updated_at] = ?
                        ,[encoding1] = ?
                        ,[encoding2] = ?
                        ,[encoding3] = ?
                        ,[encoding4] = ?
                        ,[encoding5] = ?
                        ,[encoding6] = ?
                        ,[encoding7] = ?
                        ,[encoding8] = ?
                        ,[encoding9] = ?
                        ,[encoding10] = ?
                        ,[encoding11] = ?
                        ,[encoding12] = ?
                        ,[encoding13] = ?
                        ,[encoding14] = ?
                        ,[encoding15] = ?
                        ,[encoding16] = ?
                        ,[encoding17] = ?
                        ,[encoding18] = ?
                        ,[encoding19] = ?
                        ,[encoding20] = ?
                        ,[encoding21] = ?
                        ,[encoding22] = ?
                        ,[encoding23] = ?
                        ,[encoding24] = ?
                        ,[encoding25] = ?
                        ,[encoding26] = ?
                        ,[encoding27] = ?
                        ,[encoding28] = ?
                        ,[encoding29] = ?
                        ,[encoding30] = ?
                        ,[encoding31] = ?
                        ,[encoding32] = ?
                        ,[encoding33] = ?
                        ,[encoding34] = ?
                        ,[encoding35] = ?
                        ,[encoding36] = ?
                        ,[encoding37] = ?
                        ,[encoding38] = ?
                        ,[encoding39] = ?
                        ,[encoding40] = ?
                        ,[encoding41] = ?
                        ,[encoding42] = ?
                        ,[encoding43] = ?
                        ,[encoding44] = ?
                        ,[encoding45] = ?
                        ,[encoding46] = ?
                        ,[encoding47] = ?
                        ,[encoding48] = ?
                        ,[encoding49] = ?
                        ,[encoding50] = ?
                        ,[encoding51] = ?
                        ,[encoding52] = ?
                        ,[encoding53] = ?
                        ,[encoding54] = ?
                        ,[encoding55] = ?
                        ,[encoding56] = ?
                        ,[encoding57] = ?
                        ,[encoding58] = ?
                        ,[encoding59] = ?
                        ,[encoding60] = ?
                        ,[encoding61] = ?
                        ,[encoding62] = ?
                        ,[encoding63] = ?
                        ,[encoding64] = ?
                        ,[encoding65] = ?
                        ,[encoding66] = ?
                        ,[encoding67] = ?
                        ,[encoding68] = ?
                        ,[encoding69] = ?
                        ,[encoding70] = ?
                        ,[encoding71] = ?
                        ,[encoding72] = ?
                        ,[encoding73] = ?
                        ,[encoding74] = ?
                        ,[encoding75] = ?
                        ,[encoding76] = ?
                        ,[encoding77] = ?
                        ,[encoding78] = ?
                        ,[encoding79] = ?
                        ,[encoding80] = ?
                        ,[encoding81] = ?
                        ,[encoding82] = ?
                        ,[encoding83] = ?
                        ,[encoding84] = ?
                        ,[encoding85] = ?
                        ,[encoding86] = ?
                        ,[encoding87] = ?
                        ,[encoding88] = ?
                        ,[encoding89] = ?
                        ,[encoding90] = ?
                        ,[encoding91] = ?
                        ,[encoding92] = ?
                        ,[encoding93] = ?
                        ,[encoding94] = ?
                        ,[encoding95] = ?
                        ,[encoding96] = ?
                        ,[encoding97] = ?
                        ,[encoding98] = ?
                        ,[encoding99] = ?
                        ,[encoding100] = ?
                        ,[encoding101] = ?
                        ,[encoding102] = ?
                        ,[encoding103] = ?
                        ,[encoding104] = ?
                        ,[encoding105] = ?
                        ,[encoding106] = ?
                        ,[encoding107] = ?
                        ,[encoding108] = ?
                        ,[encoding109] = ?
                        ,[encoding110] = ?
                        ,[encoding111] = ?
                        ,[encoding112] = ?
                        ,[encoding113] = ?
                        ,[encoding114] = ?
                        ,[encoding115] = ?
                        ,[encoding116] = ?
                        ,[encoding117] = ?
                        ,[encoding118] = ?
                        ,[encoding119] = ?
                        ,[encoding120] = ?
                        ,[encoding121] = ?
                        ,[encoding122] = ?
                        ,[encoding123] = ?
                        ,[encoding124] = ?
                        ,[encoding125] = ?
                        ,[encoding126] = ?
                        ,[encoding127] = ?
                        ,[encoding128] = ?
                    WHERE client_id =? and operator_id =?
                    ''')
                Values = [datetime, face_enc[0], face_enc[1], face_enc[2], face_enc[3], face_enc[4], face_enc[5], face_enc[6], face_enc[7], face_enc[8],
                        face_enc[9], face_enc[10], face_enc[11], face_enc[12], face_enc[13], face_enc[14], face_enc[15], face_enc[16], face_enc[17], face_enc[18], face_enc[19],
                        face_enc[20], face_enc[21], face_enc[22], face_enc[23], face_enc[24], face_enc[25], face_enc[26], face_enc[27], face_enc[28], face_enc[29], face_enc[30],
                        face_enc[31], face_enc[32], face_enc[33], face_enc[34], face_enc[35], face_enc[36], face_enc[37], face_enc[38], face_enc[39], face_enc[40], face_enc[41],
                        face_enc[42], face_enc[43], face_enc[44], face_enc[45], face_enc[46], face_enc[47], face_enc[48], face_enc[49], face_enc[50], face_enc[51], face_enc[52],
                        face_enc[53], face_enc[54], face_enc[55], face_enc[56], face_enc[57], face_enc[58], face_enc[59], face_enc[60], face_enc[61], face_enc[62], face_enc[63],
                        face_enc[64], face_enc[65], face_enc[66], face_enc[67], face_enc[68], face_enc[69], face_enc[70], face_enc[71], face_enc[72], face_enc[73], face_enc[74],
                        face_enc[75], face_enc[76], face_enc[77], face_enc[78], face_enc[79], face_enc[80], face_enc[81], face_enc[82], face_enc[83], face_enc[84], face_enc[85],
                        face_enc[86], face_enc[87], face_enc[88], face_enc[89], face_enc[90], face_enc[91], face_enc[92], face_enc[93], face_enc[94], face_enc[95], face_enc[96],
                        face_enc[97], face_enc[98], face_enc[99], face_enc[100], face_enc[101], face_enc[102], face_enc[103], face_enc[104], face_enc[105], face_enc[106], face_enc[107],
                        face_enc[108], face_enc[109], face_enc[110], face_enc[111], face_enc[112], face_enc[113], face_enc[114], face_enc[115], face_enc[116], face_enc[117], face_enc[118],
                        face_enc[119], face_enc[120], face_enc[121], face_enc[122], face_enc[123], face_enc[124], face_enc[125], face_enc[126], face_enc[127], client_id, r.operator_id]

                # Processing Query
                cursor.execute(SQLCommand, Values)

                conn.commit()

                result = {
                    "encoding": format(face_enc),
                    "status": True,
                    "action": 'update'
                }
                data.append(result)

    return jsonify(data), 200



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
