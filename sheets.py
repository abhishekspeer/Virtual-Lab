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
  "type": "service_account",
  "project_id": "vlab-314021",
  "private_key_id": "3112847de98e01ed2a412efebe604d4f8b71b85a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDzOWOYCYrscL0y\no/YgzlwVA3g4BUJ1196r13W6g6P3rfDSN1NOi7eAFZqY1FM4N3QYa/pvpe73YMUK\neRPm3jj0Cepe7Dvcc2YdabI8QRVX9uIUxLLcEJE7IqCdtZJT1QPY67yCqL03B/pz\n+MJd7fYtlnUeloGkglNfkBIStWvB1KaC7tFYtvbjyNWB+iUGLMmIdgXZftX21Arm\nORbFxeYjDXdCiqLlZsflIhw2S+K3spYwCQycpcMZJw8cV/yBcbvxNXlQW28z9t06\nRD9GEs7tV7bKBQMdZ0wsBRH90o73D1MM9fSJu7JIPFwMeIO8tRrpsPnOdryeJkkB\nLtBV4xjxAgMBAAECggEADzuaZbS/SySabNgA+7gA414GwvdtXKUK8Jc7a9V/yOzP\nZtMJOCOe9/oiZwzxM1Whwz/L/P8W8s5QOOIxYWWsingugghojVt62z+55nUrCYnQ\nSf2xt/+foOT/yzDKe86dAZJuCX7Y7t/kiyvavHhBUUSZjDNf5jY1U4hZ4WsUVxzD\nmWJXKb5ZE9BSFrLrgQ2N3GtfzgeB0rZ2+UHHT8N4GOry/WhKEG7msyaEseMY8OUs\nFGvzYQpqpt7NvGOWtzJVnJi5k2xgcCyVoSgNv0A9+1sWDb9TLfSyDMmbfiUgwzuH\nc9TW80Y7OfomIpfHfMIK+BqhAsh1SXG3Oylxk87jcwKBgQD6H/ALG1GKBhQp+Mkc\nG0FgfLOYDr1hGcfa5+G9AWTlLxVaayaEgazDzI/YHFcqdvRd23d/2HtDxK6XLiTw\nihseFtg5zirK8lw3dPRMxGe7jIqXIdj8vfrwRtX3cH5DAEq3PklbgYxItMjmsacE\nKcg92RiDomZxWeHWkPhfRlfClwKBgQD47/TawSdAwoy6UQa8JCQUUTHHDOFWScXS\nZIUIZu4oMO77K5Lt+eLMTWK31fwnDf9eHv2Gl5VzbjOC3U7TiMCQon2Ll2YiDfW4\nh33bqO5j5HYXV0D0bHdt6+EHi2Nla3nwg+elJ+ulkD8nWGQoYKcWf7vZiK+VhmFI\nUIx3iBPZtwKBgG3f2721SXNdSjxJymZrXqO5A9eXGf/uqEl0NUimtSCsNzAaA7iP\nkkoMsV+Yy32e9afJQcxKV5OkcaF9psJ3mIP2OxPhihDOuE2wNaUHXh4YFcVgHAai\nmfo008c3hm9+UFQAq47j8LD7oYkdnyWICSuKE2e3zlKazkdINaL8ro6PAoGAFAWA\npQN5+7xqAyY3K3Sgrj2likPf78e5MGXDSVy19OeSoQLtK1S4yAPFV9HPGPkIO/K0\nI1oXvBP18qWIDH1oN3nKLSr9HOoQhEnpdnxMyB383X24DLCYnm+lRq0QTnzpbs29\nGMxwKH3Eho6WZ6T2a1nUqvdSX+1R77YCxi5colsCgYAWhdU0KINNXwH50QiPtJs+\nt3dbHIedce0s44d4Gv1NFsEshXjPROoHMcFWOyyJh7vHtm9BQ6yscX05K7C4h90N\nDpykXxSAPv/ewg2QVdaknxWIvTVbc2B3AbuTIMuGvSAMWhmvZ0jJwlV707TgMJI3\nWEnzWS+OwEC/oWLAu9elmQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "vlaboratory@vlab-314021.iam.gserviceaccount.com",
  "client_id": "115643789993264963046",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vlaboratory%40vlab-314021.iam.gserviceaccount.com"
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
  

