"""Добавление данных в google таблицу"""

import gspread, os, datetime, json
from dotenv import load_dotenv
load_dotenv()


FILE_EXCEL_GOOGLE=os.getenv('FILE_EXCEL_GOOGLE')
WORK_SHEET_EXCEL_GOOGLE=os.getenv('WORK_SHEET_EXCEL_GOOGLE')
google_credentials = os.getenv("GOOGLE_CREDENTIALS")


if google_credentials:
    credentials_dict = json.loads(google_credentials)

    # Создаём временный JSON-файл
    temp_json_path = "service_account.json"
    with open(temp_json_path, "w") as temp_json:
        json.dump(credentials_dict, temp_json)

    # Используем его в gspread
    sa = gspread.service_account(filename=temp_json_path)

    # Можно удалить файл после загрузки (не обязательно)
    os.remove(temp_json_path)
else:
    raise ValueError("GOOGLE_CREDENTIALS не найдены в переменных окружения")

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