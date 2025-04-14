"""Добавление данных в google таблицу"""

import gspread, os, datetime
from dotenv import load_dotenv
load_dotenv()


FILE_EXCEL_GOOGLE=os.getenv('FILE_EXCEL_GOOGLE')
WORK_SHEET_EXCEL_GOOGLE=os.getenv('WORK_SHEET_EXCEL_GOOGLE')

# Путь к файлу, примонтированному в контейнер
SERVICE_ACCOUNT_FILE = "/run/secrets/credentials.json"

if os.path.exists(SERVICE_ACCOUNT_FILE):
    sa = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
else:
    raise FileNotFoundError(f"Файл {SERVICE_ACCOUNT_FILE} не найден. Убедитесь, что он смонтирован через volume.")

sh = sa.open(FILE_EXCEL_GOOGLE)
wks = sh.worksheet(WORK_SHEET_EXCEL_GOOGLE)

def data_time() -> str:
    now = datetime.datetime.now()
    return now.strftime('%d.%m.%Y %H:%M')


def adjustment_data(data: dict) -> list:
    transaction = []
    transaction.append(data_time())
    for k, v in data.items():
        transaction.append(v)
    return transaction

def add_to_google_excel(data: dict) -> bool:
    wks.append_row(adjustment_data(data=data))
    return True