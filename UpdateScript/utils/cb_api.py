import requests
from datetime import date
from decimal import Decimal
import xml.etree.ElementTree as et

import config


def get_dollar_rate() -> Decimal:
    today = date.today().strftime("%d/%m/%Y")
    data = requests.get(f"{config.CB_URL}?date_req1={today}&date_req2={today}&VAL_NM_RQ=R01235")
    return Decimal(et.fromstring(data.content.decode())[0][1].text.replace(",", "."))
