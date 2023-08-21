from aiogram.fsm.state import StatesGroup, State


# class QuestionsForTestStatesGroup(StatesGroup):
#     """Машина состояний для работы опросника - Вопросы для теста"""
#     first = State()
#     second = State()
#     third = State()
#     fourth = State()
#     fifth = State()
#     sixth = State()
#     seventh = State()
#     eighth = State()
#     ninth = State()
#     tenth = State()
#     eleventh = State()
#     twelfth = State()


class QuestionsForTestStatesGroup(StatesGroup):
    """Машина состояний для работы опросника - Вопросы для теста"""
    start = State()
    finish = State()


class ContactStatesGroup(StatesGroup):
    """Машина состояний для работы опросника по добавлению контактов"""
    number = State()
    name = State()