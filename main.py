import gspread

from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'client_secret.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
worksheet = gc.open('PIV_miguel_gut_seara').sheet1

lists = worksheet.get_all_values();
print(lists)
