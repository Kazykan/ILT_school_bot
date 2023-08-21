import sys


sys.path.append(".")
from service.pydantic_model import QuestionList


list_question = [
    {'question': '“My name’s Tamara. I __ twenty-one years old.”',
     'num': 0,
     'answer_list': [
         {'answer': ' is', 'correct': False},
         {'answer': ' am', 'correct': True},
         {'answer': ' have', 'correct': False},
         ]
     },
    {'question': '“Is Igor a teacher?” “ No, __ .”',
     'num': 1,
     'answer_list': [
         {'answer': 'he not', 'correct': False},
         {'answer': "he doesn't", 'correct': False},
         {'answer': "he isn't", 'correct': True}
         ]
     },
    {'question': 'Igor and Tamara are __ people.',
     'num': 2,
     'answer_list': [
         {'answer': 'teachers', 'correct': False},
         {'answer': 'nice', 'correct': True},
         {'answer': 'long', 'correct': False}
         ]
     },
    {'question': 'My brother  __ like to go to school.',
     'num': 3,
     'answer_list': [
         {'answer': "doesn't", 'correct': True},
         {'answer': "don't", 'correct': False},
         {'answer': 'not', 'correct': False}
         ]
     },
    {'question': '__ milk in the bottle.',
     'num': 4,
     'answer_list': [
         {'answer': 'it is any', 'correct': False},
         {'answer': 'there is any', 'correct': False},
         {'answer': 'there is some', 'correct': True}
         ]
     },
    {'question': '“__________ you speak English, Igor?” “Yes, a little.”',
     'num': 5,
     'answer_list': [
         {'answer': 'has', 'correct' : False},
         {'answer': 'can', 'correct': True},
         {'answer': 'are', 'correct': False}
         ]
     },
     {'question': 'My friend and I  __.',
     'num': 6,
     'answer_list': [
         {'answer': 'like rock both.', 'correct': False},
         {'answer': 'both like rock', 'correct' : True},
         {'answer': 'like both rock', 'correct': False}
         ]
     },
     {'question': 'I __ the Beatles last year, but now I do.',
     'num': 7,
     'answer_list': [
         {'answer': 'not like', 'correct': False},
         {'answer': "didn't like", 'correct' : True},
         {'answer': "didn't liked", 'correct': False}
         ]
     },
     {'question': 'My mother  __ me to buy some bread from the shop.',
     'num': 8,
     'answer_list': [
         {'answer': 'said', 'correct': False},
         {'answer': 'told', 'correct': True},
         {'answer': 'say to', 'correct' : False}
         ]
     },
     {'question': 'Have you __ been to Paris?',
     'num': 9,
     'answer_list': [
         {'answer': 'often', 'correct': False},
         {'answer': 'never', 'correct': False},
         {'answer': 'ever', 'correct' : True}
         ]
     },
]


list_question_old = [
    {'question': 'Выберите наиболее подходящий ответ! "What does your husband do?"',
     'num': 0,
     'answer_list': [
         {'answer': 'He is feeding the dog.', 'correct': False},
         {'answer': 'He is a doctor.', 'correct': True},
         {'answer': 'Yes, he does.', 'correct': False},
         ]
     },
    {'question': 'Yesterday I ................. a bird',
     'num': 1,
     'answer_list': [
         {'answer': 'saw', 'correct': True},
         {'answer': 'sawed', 'correct': False},
         {'answer': 'see', 'correct': False}
         ]
     },
    {'question': 'Найдите неправильный глагол: to smile, to laugh, to see.',
     'num': 2,
     'answer_list': [
         {'answer': 'to see', 'correct': True},
         {'answer': 'to smile', 'correct': False},
         {'answer': 'to laugh', 'correct': False}
         ]
     },
    {'question': 'Укажите существительное, имеющее неправильную форму множественного числа.',
     'num': 3,
     'answer_list': [
         {'answer': 'lady', 'correct': False},
         {'answer': 'gentleman', 'correct': True},
         {'answer': 'son', 'correct': False}
         ]
     },
    {'question': 'Найдите ошибку в трёх формах глагола:',
     'num': 4,
     'answer_list': [
         {'answer': 'teach – taught – taught', 'correct': False},
         {'answer': 'catch – caught – caught', 'correct': False},
         {'answer': 'bring – braught – braught', 'correct': True}
         ]
     },
    {'question': 'Выберите наиболее подходящий ответ! "What is she doing?"',
     'num': 5,
     'answer_list': [
         {'answer': 'She is playing with the bunny.', 'correct': True},
         {'answer': 'She cleans the house every day.', 'correct' : False},
         {'answer': 'She is a manager', 'correct': False}
         ]
     },
     {'question': 'Karina never minds ................. the movie again',
     'num': 6,
     'answer_list': [
         {'answer': 'to be watched.', 'correct': False},
         {'answer': 'watching.', 'correct' : True},
         {'answer': 'to watch', 'correct': False}
         ]
     },
     {'question': 'I couldn’t help ................. .',
     'num': 7,
     'answer_list': [
         {'answer': 'for laughing', 'correct': False},
         {'answer': 'laughing', 'correct' : True},
         {'answer': 'to laughed', 'correct': False}
         ]
     },
     {'question': 'Можно мне взять Ваш карандаш?',
     'num': 8,
     'answer_list': [
         {'answer': 'Can I take your pencil?', 'correct': False},
         {'answer': 'Must I take your pencil?', 'correct' : False},
         {'answer': 'May I take your pencil?', 'correct': True}
         ]
     },
     {'question': 'Марта никогда не слышала, как он говорит по-английски.',
     'num': 9,
     'answer_list': [
         {'answer': 'Martha never heard him spoke English.', 'correct': False},
         {'answer': 'Martha has never heard him speak English.', 'correct' : True},
         {'answer': 'Martha never heard how he speaks English.', 'correct': False}
         ]
     },
     {'question': 'Я знаю его четыре года.',
     'num': 10,
     'answer_list': [
         {'answer': 'I know him four years.', 'correct': False},
         {'answer': 'I know him for four years.', 'correct' : False},
         {'answer': 'I have known him for four years.', 'correct': True}
         ]
     },
     {'question': 'В каком из представленных ниже слов звук, который передаётся буквой «a», отличается от остальных:',
     'num': 11,
     'answer_list': [
         {'answer': 'map', 'correct': True},
         {'answer': 'tape', 'correct' : False},
         {'answer': 'make', 'correct': False}
         ]
     },
     {'question': 'I have ................. butter, please, buy some.',
     'num': 12,
     'answer_list': [
         {'answer': 'little', 'correct': True},
         {'answer': 'few', 'correct' : False},
         {'answer': 'a few', 'correct': False}
         ]
     },
     {'question': 'The taxi ................. by 7 o’clock yesterday.',
     'num': 13,
     'answer_list': [
         {'answer': 'has arrived', 'correct': False},
         {'answer': 'arrived', 'correct' : False},
         {'answer': 'had arrived', 'correct': True}
         ]
     },
     {'question': 'Должно быть, он продал свою машину.',
     'num': 14,
     'answer_list': [
         {'answer': 'It must be that he has sold his car.', 'correct': False},
         {'answer': 'He must sold his car.', 'correct' : False},
         {'answer': 'He must have sold his car.', 'correct': True}
         ]
     },
     {'question': 'Я хочу, чтобы погода была хорошая.',
     'num': 15,
     'answer_list': [
         {'answer': 'I want that the weather will be fine.', 'correct': False},
         {'answer': 'I want the weather to be fine.', 'correct' : True},
         {'answer': 'I want the weather be fine.', 'correct': False}
         ]
     },
]
