import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


def get_credentials(credentials, scopes):
    # Get creds only from file, and authenticate every time
    flow = InstalledAppFlow.from_client_secrets_file(credentials, scopes)
    creds = flow.run_local_server(port=0)
    return creds


def refrest_credentials(creds):
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        raise ValueError("Unable to refresh credentials.")
