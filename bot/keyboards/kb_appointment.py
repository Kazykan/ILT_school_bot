from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.cbdata import AppointmentCFactory, QuestionsCFactory
from service.pydantic_model import Question
from service.questions import list_question



def get_keyboard_appointment():
    """Две кнопки записи на тестирование"""
    builder = InlineKeyboardBuilder()
    builder.button(text=f'Да',
                   callback_data=AppointmentCFactory(answer=f'Yes'))
    builder.button(text=f'Нет',
                   callback_data=AppointmentCFactory(answer=f'No'))
    builder.adjust(2)
    return builder.as_markup()