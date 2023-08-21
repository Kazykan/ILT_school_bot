import locale, sys

sys.path.append(".")
from service.dbworker import session, Client


def is_bot_user_id(bot_user_id: int):
    """Поиск в БД есть такой пользователь"""
    parent = session.query(Client).filter(Client.bot_user_id == bot_user_id).first()
    if parent is None:
        return False
    else:
        return True


def add_client_db(bot_user_id, name, phone):
    """Добавление нового клиента"""
    client = Client(
        bot_user_id = bot_user_id,
        name = name,
        phone = phone,
    )
    session.add(client)
    session.commit()