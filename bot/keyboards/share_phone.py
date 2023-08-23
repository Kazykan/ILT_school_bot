from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def kb_share_phone() -> types.KeyboardButton:
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Поделиться номером ☎️", request_contact=True))
    return builder.as_markup(resize_keyboard=True)