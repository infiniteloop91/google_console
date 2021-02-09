import  gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.metadata'
  ]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("TEST_SHEET")

# data = sheet.get_all_records()

content = open('MOCK_DATA.csv', 'r').read()
client.import_csv(sheet.id,content)
