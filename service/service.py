import re

from bot.text import CORRECT_ANSWER_END, ELEMENTARY, ELEMENTARY_CORRECT_ANSWER, PRE_INTERMEDIATE, PRE_INTERMEDIATE_CORRECT_ANSWER, STARTER_CORRECT_ANSWER, STARTER, TEST_END_TEXT, WOW_CORRECT_ANSWER


def valid_number(number: str):
    """Проверка номера на валидность"""
    num = ''.join([x for x in number if x.isdigit()])
    if len(num) == 11: num = '7' + num[1:]
    elif len(num) == 10: num = '7' + num
    try:
        result = re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', num)
        if bool(result): return num
        else: return False
    except TypeError: return False


def valid_name(contact):
    fullname = ''
    if contact.last_name:
        fullname += f'{contact.last_name} '
    if contact.first_name:
        fullname += f'{contact.first_name}'
    if fullname == '':
        pass
    return fullname


def test_results_text(answer_points: int) -> str:
    text = ''
    if answer_points <= 4:
        text += f"{STARTER_CORRECT_ANSWER} {answer_points} {CORRECT_ANSWER_END}{STARTER}"
    elif answer_points <= 7:
        text += f"{ELEMENTARY_CORRECT_ANSWER} {answer_points} {CORRECT_ANSWER_END}{ELEMENTARY}"
    elif answer_points <= 9:
        text += f"{PRE_INTERMEDIATE_CORRECT_ANSWER} {answer_points} {CORRECT_ANSWER_END}{PRE_INTERMEDIATE}"
    elif answer_points == 10:
        text += f"{WOW_CORRECT_ANSWER} {answer_points} {CORRECT_ANSWER_END}"  
    text += f"{TEST_END_TEXT}"
    return text
    
def format_client_data(data: dict) -> str:
    """Форматирует данные клиента для отправки админу"""
    return (
        f"👤 <b>Имя:</b> {data.get('name')}\n"
        f"📞 <b>Телефон:</b> <code>{data.get('phone')}</code>\n"
        f"🆔 <b>Bot User ID:</b> {data.get('bot_user_id')}\n"
        f"🎮 <b>Никнейм:</b> {data.get('nickname') or '—'}\n"
        f"📌 <b>Оценка:</b> {data.get('answer_point') or '—'} из 10\n"
        f"📝 <b>Ответ:</b> {data.get('answer_text') or '—'}\n"
        f"📅 <b>Запись на приём:</b> {'Да' if data.get('appointment') else 'Нет'}"
    )

