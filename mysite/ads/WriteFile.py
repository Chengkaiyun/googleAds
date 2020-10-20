from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
SPREADSHEET_ID = '1u63Boe17Nvq9T1SitNA6Ht4UqLcZVYgaXqHWyAm5v6U'
# How the input data should be interpreted.
value_input_option = 'RAW'
# How the input data should be inserted.
insert_data_option = 'INSERT_ROWS'

BODY_CLEAR = {}
RANGE_INPUT_TW = 'TW!A1:ZZ'
RANGE_INPUT_IO = 'IO!A1:ZZ'
RANGE_INPUT_FR = 'FR!A1:ZZ'



def input_sheets(Country, body):
    if Country == "TW":
        RANGE_INPUT = RANGE_INPUT_TW
    elif Country == "FR":
        RANGE_INPUT = RANGE_INPUT_FR
    elif Country == "IO":
        RANGE_INPUT = RANGE_INPUT_IO


    request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID, \
                                                     range=RANGE_INPUT, \
                                                     valueInputOption=value_input_option, \
                                                     insertDataOption=insert_data_option, \
                                                     body=body)
    response = request.execute()

def clear_sheets(Country):
    if Country == "TW":
        RANGE_INPUT = RANGE_INPUT_TW
    elif Country == "FR":
        RANGE_INPUT = RANGE_INPUT_FR
    elif Country == "IO":
        RANGE_INPUT = RANGE_INPUT_IO

    request = service.spreadsheets().values().clear(spreadsheetId=SPREADSHEET_ID, \
                                                     range=RANGE_INPUT,\
                                                     body=BODY_CLEAR)
    response = request.execute()

def main(Country, DataList):

    BODY_INPUT = {
        'values': DataList ,
        'majorDimension': 'ROWS',
    }

    clear_sheets(Country)
    input_sheets(Country, BODY_INPUT)

