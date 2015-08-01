import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import config

def get_worksheet():
    json_key = json.load(open(config.json_file))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(
            json_key['client_email'],
            json_key['private_key'], scope)
    gc = gspread.authorize(credentials)
    sh = gc.open(config.spreadsheet)
    return sh.worksheet(config.worksheet)
