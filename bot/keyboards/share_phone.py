from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def kb_share_phone() -> types.KeyboardButton:
    builder = ReplyKeyboardBuilder()
    # метод row позволяет явным образом сформировать ряд
    # из одной или нескольких кнопок. Например, первый ряд
    # будет состоять из двух кнопок...
    builder.add(types.KeyboardButton(text="Поделиться номером ☎️", request_contact=True))
    return builder.as_markup(resize_keyboard=True)