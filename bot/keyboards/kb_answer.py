
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.cbdata import QuestionsCFactory
from service.pydantic_model import Question
from service.questions import list_question



def get_keyboard_with_answers(number_question: int):
    """Три кнопки с ответами один из них помечен как правильный"""
    builder = InlineKeyboardBuilder()
    question = Question(**list_question[number_question])
    for i in question.answer_list:
        builder.button(
            text=f'{i.answer}',  # TODO: Убрать {i.correct}
            callback_data=QuestionsCFactory(
                num=(number_question + 1),
                answer=f'{i.correct}',
                answer_text=f'{i.answer}')
            ) 
    builder.adjust(1)
    return builder.as_markup()