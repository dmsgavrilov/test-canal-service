import sys
import time
import logging
from decimal import Decimal

import psycopg2 as psql

from utils.cb_api import get_dollar_rate
from utils.sheets_api import get_sheets_data, check_delivery_date
from utils.telegram_api import send_notify
import config

logging.basicConfig(
    format=config.MESSAGE_FORMAT,
    datefmt=config.DATE_FORMAT,
    stream=sys.stdout,
    level=logging.INFO
)

conn = psql.connect(config.DATABASE_URI)


def monitor_spreadsheet() -> None:
    while True:
        sheets_data = get_sheets_data()
        logging.info("Received spreadsheets data")

        dollar_rate = get_dollar_rate()
        logging.info("Received dollar rate")

        conn.cursor().execute(
            "DELETE FROM orders"
        )
        conn.commit()
        logging.info("Clear orders table")

        for i, row in enumerate(sheets_data):
            delivery_date_lst = row[2].split(".")
            delivery_date_lst.reverse()
            delivery_date = "-".join(delivery_date_lst)
            order_id = int(row[0])
            price_usd = Decimal(row[1])
            price_rub = Decimal(row[1]) * dollar_rate
            conn.cursor().execute(
                f"INSERT INTO orders "
                f"(order_id, delivery_date,"
                f" price_usd, price_rub) VALUES ("
                f"{order_id}, '{delivery_date}', "
                f"{price_usd}, {price_rub});"
            )
            if (i + 1) % 10 == 0 or i + 1 == len(sheets_data):
                logging.info(f"Add {i + 1} rows")
            if not check_delivery_date(delivery_date):
                send_notify(order_id)
                time.sleep(config.TELEGRAM_TIMEOUT)
        conn.commit()
        logging.info("Finish, table orders is updated")
        time.sleep(config.REQUEST_TIMEOUT)
