import locale, sys

sys.path.append(".")
from service.dbworker import session, Client


def is_bot_user_id(bot_user_id: int):
    """Поиск в БД есть такой пользователь"""
    client = session.query(Client).filter(Client.bot_user_id == bot_user_id).first()
    if client is None:
        return False
    else:
        return True


def add_client_db(bot_user_id, name, phone, nickname):
    """Добавление нового клиента"""
    client = Client(
        bot_user_id = bot_user_id,
        name = name,
        phone = phone,
        nickname = nickname
    )
    session.add(client)
    session.commit()


def edit_client_answer(bot_user_id: int, answer_text: list, answer_point: int):
    """Добавляем данные по клиенту"""
    client = session.query(Client).filter(Client.bot_user_id == bot_user_id).first()
    client.answer_text = answer_text
    client.answer_point = answer_point
    session.commit()
    return True


def edit_client_appointment(bot_user_id: int, appointment: bool):
    """Добавляем данные по клиенту"""
    client = session.query(Client).filter(Client.bot_user_id == bot_user_id).first()
    client.appointment = appointment
    session.commit()
    return True


def get_client(bot_user_id: int):
    client = session.query(Client).filter(Client.bot_user_id == bot_user_id).first()
    return client.serialize
    