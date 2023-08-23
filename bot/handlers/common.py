from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from bot.keyboards.for_start import ikb_start
from bot.keyboards.share_phone import kb_share_phone
from bot.statesgroup import ContactStatesGroup
from bot.text import WELCOME_TEXT, START_TEST
from service.db_service import is_bot_user_id



router = Router()


@router.message(Command('cancel'))
@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()  # Clear FSM
    if is_bot_user_id(bot_user_id=int(message.from_user.id)):
        await message.answer(text=START_TEST,
                        reply_markup=ikb_start())
    else:
        await message.answer(
            text=WELCOME_TEXT,
            reply_markup=kb_share_phone())
        await state.set_state(ContactStatesGroup.number)


