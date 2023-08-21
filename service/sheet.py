"""Добавление данных в google таблицу"""

import gspread
import datetime

from conf import FILE_EXCEL_GOOGLE, WORK_SHEET_EXCEL_GOOGLE


sa = gspread.service_account(filename='service_account.json')
sh = sa.open(FILE_EXCEL_GOOGLE)
wks = sh.worksheet(WORK_SHEET_EXCEL_GOOGLE)

def data_time() -> str:
    now = datetime.datetime.now()
    return now.strftime('%d.%m.%Y %H:%M')


def adjustment_data(data: dict) -> list:
    transaction = []
    for k, v in data.items():
        transaction.append(v)
    transaction.append(data_time())
    return transaction

def add_to_google_excel(data: dict) -> bool:
    wks.append_row(adjustment_data(data=data))
    return True