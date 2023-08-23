from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.cbdata import AppointmentCFactory, QuestionsCFactory
from service.pydantic_model import Question
from service.questions import list_question



def get_keyboard_link():
    """Две кнопки записи на тестирование"""
    builder = InlineKeyboardBuilder()
    builder.button(text='ILT School Channel',
                   url="https://t.me/iltschool")
    builder.adjust(1)
    return builder.as_markup()