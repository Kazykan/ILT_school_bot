from datetime import date
from typing import Optional
from aiogram.filters.callback_data import CallbackData


class QuestionsCFactory(CallbackData, prefix="cb_questions"):
    """Префикс — это общая подстрока в начале, по которой фреймворк будет определять, какая структура лежит в колбэке"""
    num: int
    answer: str