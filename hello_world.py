import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import re


scope = ["https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "./google-api/credentials.json", scope
)
gc = gspread.authorize(credentials)

print(gc)

url = "https://docs.google.com/spreadsheets/d/1cBjkiCuqg-N3gAEhtg-f7Gcl1ViF5rr5jY05LengEdk/edit#gid=0"

sheet_id = re.findall(r"https://docs.google.com/spreadsheets/d/(\S+)/", url)[0]
print(sheet_id)


book = gc.open_by_key(sheet_id)
worksheet = book.worksheet("Candidate Data")
table = worksheet.get_all_values()
