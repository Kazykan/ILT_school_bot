"""Тестирование"""
import sys

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext


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
            text=f"1 из 15. {question.question}",
            reply_markup=get_keyboard_with_answers(number_question=0)
            )
        await state.update_data(answer_points=0)
        await state.set_state(QuestionsForTestStatesGroup.start)
    elif callback_data.num != 15:
        question = Question(**list_question[callback_data.num])
        data = await state.get_data()
        if callback_data.answer == True or callback_data.answer == 'True':
            await state.update_data(answer_points=data["answer_points"] + 1)
        data = await state.get_data()
        await callback.message.edit_text(
            text=f'{callback_data.num + 1} из 15. {question.question}\n{data["answer_points"]}',
            reply_markup=get_keyboard_with_answers(number_question=callback_data.num)
            )
        await state.set_state(QuestionsForTestStatesGroup.start)
    else:
        data = await state.get_data()
        if callback_data.answer == True or callback_data.answer == 'True':
            await state.update_data(answer_points=data["answer_points"] + 1)
        data = await state.get_data()
        await callback.message.edit_text(text=f'Вы ответили правильно на {data["answer_points"]} из 15 вопросов')
        await state.clear()