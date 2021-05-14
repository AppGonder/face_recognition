
import face_recognition
from sklearn import svm
import os
import pyodbc
# Training the SVC classifier
import urllib.request
import boto3
import requests

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


# The training data would be all the face encodings from all the known images and the labels are their names
encodings = []
names = []

# Training directory

SQL = "selecT aws_tag as aws_key, name as name, registration as registration from operators where client_id = '1' and file_name <> '' and id = 38"
cursor = conn.cursor()
cursor.execute(SQL)
row = cursor.fetchall()

# Loop through each person in the training directory
for person in row:

    client_id = '1'

    s3 = boto3.client('s3')
    # Generate the URL to get 'key-name' from 'bucket-name'
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'siftmov',
            'Key': 'operadores/' + client_id + '/' + person.aws_key
        }
    )

    response = urllib.request.urlopen(url)

    # Get the face encodings for the face in each image file
    face = face_recognition.load_image_file(response)
    face_bounding_boxes = face_recognition.face_locations(face)

    face_enc = face_recognition.face_encodings(face)[0]

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
    Values = ['1', '2021-05-07 14:58', '', '30', face_enc[0], face_enc[1], face_enc[2], face_enc[3], face_enc[4], face_enc[5], face_enc[6], face_enc[7], face_enc[8],
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
    print("Data Successfully Inserted")
    conn.close()
