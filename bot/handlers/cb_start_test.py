"""Тестирование"""
import sys

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.keyboards.kb_appointment import get_keyboard_appointment
from service.db_service import edit_client_answer

from service.service import test_results_text


sys.path.append("..")
from bot.cbdata import QuestionsCFactory
from service.pydantic_model import Question
from service.questions import list_question
from bot.statesgroup import QuestionsForTestStatesGroup
# from bot.keyboards.kb_general import ikb_gender
from bot.keyboards.kb_answer import get_keyboard_with_answers


router = Router()

@router.callback_query(QuestionsCFactory.filter())
async def cb_add_one_more_parent(callback: types.CallbackQuery,
                                 state: FSMContext,
                                 callback_data: QuestionsCFactory
                                 ) -> None:
    """Первый пункт опросника по тестированию"""
    if callback_data.num == 0:
        question = Question(**list_question[0])
        await callback.message.edit_text(
            text=f"1 из 10. {question.question}",
            reply_markup=get_keyboard_with_answers(number_question=0)
            )
        await state.update_data(answer_points=0)
        await state.update_data(answer_text=[])
        await state.set_state(QuestionsForTestStatesGroup.start)
    elif callback_data.num != 10:
        question = Question(**list_question[callback_data.num])
        data = await state.get_data()
        if callback_data.answer == True or callback_data.answer == 'True':
            await state.update_data(answer_points=data["answer_points"] + 1)

        data = await state.get_data()
        answer_text = f'{callback_data.answer} - {callback_data.answer_text}'
        await state.update_data(data["answer_text"].append(answer_text))

        await callback.message.edit_text(
            text=f'{callback_data.num + 1} из 10. {question.question}',
            reply_markup=get_keyboard_with_answers(number_question=callback_data.num)
            )  # {data["answer_points"]}
        await state.set_state(QuestionsForTestStatesGroup.start)
    else:
        data = await state.get_data()
        if callback_data.answer == True or callback_data.answer == 'True':
            await state.update_data(answer_points=data["answer_points"] + 1)

        data = await state.get_data()
        answer_text = f'{callback_data.answer} - {callback_data.answer_text}'
        await state.update_data(data["answer_text"].append(answer_text))

        #  {data["answer_text"]} = ['True -  am', "False - he doesn't", 'False - long', "False - don't", 'False - it is any', 'False - are', 'True - both like rock', "False - didn't liked", 'False - said', 'False - never']

        data = await state.get_data()

        edit_client_answer(
            bot_user_id=int(callback.from_user.id),
            answer_text=f'{data["answer_text"]}',
            answer_point=data["answer_points"])
        
        await callback.message.edit_text(
            text=f'{test_results_text(answer_points=data["answer_points"])}',
            reply_markup=get_keyboard_appointment())
        
        await state.clear()