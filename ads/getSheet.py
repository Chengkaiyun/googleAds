from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import ads.globals as Var
import mysite.settings as Settings
import pandas as pd

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1mnkC4um-dlzoA7C-AYhPxyg7rmsLPa7hKgHZgsTikLI'

def main(sheetName):
    RANGE_NAME = sheetName + '!A2:J'
    DATA_NAME = 'info!B1:J'

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            JSON_FILE = os.path.join(Settings.BASE_DIR, 'client_secret.json')
            print(JSON_FILE)
            flow = InstalledAppFlow.from_client_secrets_file(JSON_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()

    # =============================== get Data =============================== #
    # 讀取 info 頁面資訊
    try:
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=DATA_NAME).execute()
        Var.countryInfo = result.get('values', [])
        Var.countryInfo = pd.DataFrame(Var.countryInfo[1:],columns=Var.countryInfo[0])

        # 讀取 行銷產品 頁面資訊
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME,
                                    majorDimension='COLUMNS').execute()
    except:
        return True

    data = result.get('values', [])
    Var.sku = data[1]
    Var.designSku = data[2]
    Var.productLine = data[4]
    Var.device = data[5]
    Var.caseColor = data[6]
    Var.bumperColor = data[7]

    if not data:
        print('No design found.')
    else:
        print("Get Data")


