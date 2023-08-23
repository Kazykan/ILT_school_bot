from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.cbdata import QuestionsCFactory


def ikb_start() -> types.InlineKeyboardButton:
    """Кнопки первые: выбор родитель или ребенок"""
    builder = InlineKeyboardBuilder()
    builder.button(
            text=f'Начать тестирование',
            callback_data=QuestionsCFactory(num=0, answer='not', answer_text='not')) 
    builder.adjust(1)
    return builder.as_markup()