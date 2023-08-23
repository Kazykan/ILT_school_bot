"""Добавление номера телефона"""
import sys

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.keyboards.for_start import ikb_start
from bot.text import START_TEST
from service.db_service import add_client_db
from service.sheet import add_to_google_excel


sys.path.append("..")
from service.service import valid_name, valid_number
from bot.statesgroup import ContactStatesGroup


router = Router()


@router.message(F.contact,
                ContactStatesGroup.number)
async def cb_add_client_number_phone(message: types.Message, state: FSMContext) -> None:
    contact = message.contact  # Получем его данные
    fullname = valid_name(contact)
    phone_number = valid_number(contact.phone_number)
    add_client_db(
        bot_user_id=contact.user_id,
        phone=phone_number,
        name=fullname,
        nickname=f'@{message.from_user.username}')
    data = {}
    data['name'] = fullname
    data['phone_number'] = valid_number(contact.phone_number)
    data['bot_user_id'] = contact.user_id
    data['contact_nickname'] = f'@{message.from_user.username}'
    add_to_google_excel(data=data)
    await state.clear()
    await message.answer(f"{fullname}",
                        parse_mode="HTML",
                        reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=START_TEST,
            reply_markup=ikb_start())
    