from pydantic import BaseModel
from typing import List
# from datetime import datetime, date

class Answer(BaseModel):
    answer: str
    correct: bool


class Question(BaseModel):
    question: str
    num: int
    answer_list: List[Answer]


class QuestionList(BaseModel):
    quest_list: List[Question]


class AnswerList(BaseModel):
    answer_list: List[Answer]

