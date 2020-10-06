from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import ads.globals as Var
import mysite.settings as Settings
import pandas as pd
import os

# Setup the Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    JSON_FILE = os.path.join(Settings.BASE_DIR, 'client_secret.json')
    print(JSON_FILE)
    flow = client.flow_from_clientsecrets(JSON_FILE, SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))


# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1mnkC4um-dlzoA7C-AYhPxyg7rmsLPa7hKgHZgsTikLI'
# How the input data should be interpreted.
value_input_option = 'RAW'
# How the input data should be inserted.
insert_data_option = 'INSERT_ROWS'


def main(sheetName):
    RANGE_NAME = sheetName + '!A2:J'
    DATA_NAME = 'info!B1:J'

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


