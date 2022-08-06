import os

# Database
DATABASE_URI = os.getenv("DATABASE_URI", "postgres://postgres:123@localhost:5432")

# logging
DATE_FORMAT = "%d-%b-%y %H:%M:%S"
MESSAGE_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Spreadsheets
SPREADSHEET_ID = "1NKughm4IIRRMi5Di57CUNgKccxIcFk5c958rfwL5TCQ"
GOOGLE_CREDENTIALS = "creds.json"

# Telegram
BOT_TOKEN = "5407170492:AAH5-L5Y9BaB7ufh3JGjZRmpCQPyvYPqz_U"
TEST_NOTIFY_CHANNEL = "@not1fy_test_channel"
TEMPLATE_TEXT = "text=Заказ №%s:\nИстек срок поставки"
NOTIFY_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/" \
             f"sendMessage?chat_id={TEST_NOTIFY_CHANNEL}&{TEMPLATE_TEXT}"

# Timeouts
REQUEST_TIMEOUT = 600  # 10 minutes
TELEGRAM_TIMEOUT = 3.01  # min interval between messages

# Others
CB_URL = "http://www.cbr.ru/scripts/XML_dynamic.asp"
