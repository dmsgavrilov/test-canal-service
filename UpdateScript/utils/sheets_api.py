import os.path
from datetime import datetime
from typing import List, Optional

from googleapiclient.discovery import build
from google.oauth2 import service_account

import config

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, config.GOOGLE_CREDENTIALS)

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build("sheets", "v4", credentials=credentials).spreadsheets().values()


def get_sheets_data() -> Optional[List[List[str]]]:
    values = service.get(
        spreadsheetId=config.SPREADSHEET_ID,
        range="B2:D",
        majorDimension="ROWS"
    ).execute()
    return values["values"]


def check_delivery_date(delivery_date: str) -> bool:
    delivery_date = datetime.strptime(delivery_date, "%Y-%m-%d")
    if delivery_date > datetime.now():
        return True
    return False
