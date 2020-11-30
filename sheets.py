import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint 
  
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', 
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"] 
  
  
  
# Assign credentials ann path of style sheet 
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) 
client = gspread.authorize(creds) 
sheet = client.open("LOP Database").sheet1 
 
  
def loginverify(username,password):
	try:
 	 
# Sisplay data 
		data = sheet.get_all_records() 
		userid=[]
		usernameslist = sheet.col_values(2)
	
		k=0;
		#cell = sheet.cell(4, 1).value 
		for i in usernameslist	:
			k=k+1
			if username in i: 
				userid=(sheet.row_values(k))
				
		if userid[1]!=username :
			return 0
			
			
		if userid[2]==password:
			return userid
		else :
			return 0
	except:
		return 0


def getDetails(username):
	try:
		data = sheet.get_all_records() 
		userid=[]
		usernameslist = sheet.col_values(2)
		
		k=0;
		#cell = sheet.cell(4, 1).value 
		for i in usernameslist	:
			k=k+1
			if username in i: 
				userid=(sheet.row_values(k))
				return userid
	except:
		return ['0','invalid','invalid','invalid','invalid','invalid','invalid','invalid']				