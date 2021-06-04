import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaIoBaseUpload
from datetime import datetime
import os.path
from io import BytesIO
import sys
from base64 import urlsafe_b64encode
from email.mime.text import MIMEText

credentials = {
  "Service account details"
}

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', 
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive",
         ] 

creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials,scope)

#creds = ServiceAccountCredentials.service_account_from_dict(credentials, scope)
client = gspread.authorize(creds)
try:
        sheet = client.open("Creds_Vlab").sheet1
except:
        sheet = client.open("LOP Database").sheet1
def loginverify(username,password):
        try:
                #data = sheet.get_all_records() 
                userid=[]
                usernameslist = sheet.col_values(2)
        
                k=0;
                #cell = sheet.cell(4, 1).value 
                for i in usernameslist  :
                        k=k+1
                        if username == i: 
                                userid = [sheet.cell(k, 2).value, sheet.cell(k, 3).value]
                                break
                                
                if userid[0]!=username :
                        return (0, 0, 0)
                        
                        
                if userid[1]==password:
                        return (1, getDetails(username, k), k)
                else :
                        return (0, 0, 0)
        except:
                return (0,0,0)

def SUBMITDATA(username, exp, data, k):
        try:
                EXP = client.open("LOP Database")
                temp = EXP.get_worksheet(exp)
                if(temp.cell(k, 2).value == username):
                        
                        flag = 0
                        for i in data:
                                temp.update_cell(k, 3+flag, str(i))
                                flag+=1
                        return 1
                else:
                        return 0
        except:
                return 0
                        
def getDetails(username, k):
        try:
                if(sheet.cell(k, 2).value == username):
                        userid = sheet.row_values(k)
                        return userid
                return None
        except:
                return None

def fetchDetails(username):
        try:
                usernameslist = sheet.col_values(2)
        
                k=0
                for i in usernameslist  :
                        k=k+1
                        if username == i:
                                #print("in here")
                                userid = [sheet.cell(k, 2).value, sheet.cell(k, 3).value]
                                return userid
                return None
        except:
                return None
                        
                
        
def UPLOADONDRIVE2(DATA_Misc, dataGEN, dataIN, labels, folder_id="1FJDYxVhN3e5_bs2TFC9VlUzS3S3JuXhU"):
        try:
                #print("Calling the authenticator")
                service = build('drive', 'v3', credentials=creds, static_discovery=False)        
                
                stringdata = str(DATA_Misc[0])+"\n\n"+str(DATA_Misc[2])+"\n"+str(DATA_Misc[1])

                stringdata = stringdata + "\n\n-----:GENERATED:-----\n"

                flag = 0
                for i in dataGEN:
                        stringdata = stringdata+str(labels[flag])+"->"+str(i)+"\n"
                        flag+=1
                flag = 0
                stringdata = stringdata + "\n\n-----:USER INPUT:-----\n"
                for i in dataIN:
                        stringdata = stringdata+str(labels[flag])+"->"+str(i)+"\n"
                        flag+=1
                
                bio = BytesIO(stringdata.encode())
                #print(bio)
                file_meta = {"name": str(str(DATA_Misc[0])+"_"+str(DATA_Misc[1])+".txt"),
                             "parents": [folder_id]}
                
                media = MediaIoBaseUpload(bio, mimetype='text/plain',
                                          resumable=True)
                #file3 = file1.get('id')
                request = service.files().create(body=file_meta, media_body=media,
                                                 fields = 'id').execute()
                #print("Upload Complete")
                #remove(str(userID+".txt"))
                return 1
        except:
                #remove(userID+".txt")
                return 0
  

