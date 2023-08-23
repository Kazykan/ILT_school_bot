"""Запись на тестирование"""
import sys

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.keyboards.kb_appointment import get_keyboard_appointment
from bot.keyboards.kb_link import get_keyboard_link
from bot.text import YES_TEXT, NO_TEXT
from service.db_service import edit_client_appointment, get_client

from service.service import test_results_text
from service.sheet import add_to_google_excel


sys.path.append("..")
from bot.cbdata import AppointmentCFactory
from service.pydantic_model import Question
from service.questions import list_question
from bot.statesgroup import QuestionsForTestStatesGroup
# from bot.keyboards.kb_general import ikb_gender
from bot.keyboards.kb_answer import get_keyboard_with_answers


router = Router()


@router.callback_query(AppointmentCFactory.filter())
async def cb_add_one_more_parent(callback: types.CallbackQuery,
                                callback_data: AppointmentCFactory) -> None:
    """Обработка кнопок ответа"""
    if callback_data.answer == 'yes':
        edit_client_appointment(
            bot_user_id=int(callback.from_user.id),
            appointment=True)
        await callback.message.edit_text(
            text=YES_TEXT,
            reply_markup=get_keyboard_link())
    else:
        edit_client_appointment(
            bot_user_id=int(callback.from_user.id),
            appointment=False)
        await callback.message.edit_text(
            text=NO_TEXT,
            reply_markup=get_keyboard_link())
    
    data = get_client(bot_user_id=int(callback.from_user.id))
    add_to_google_excel(data=data)

    