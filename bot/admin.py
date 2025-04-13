import os
from dotenv import load_dotenv
from aiogram import Bot
from service.service import format_client_data


load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_TELEGRAM_ID = os.getenv("ADMIN_TELEGRAM_ID")


bot = Bot(token=TELEGRAM_TOKEN)


async def notify_admin(data: dict):
    """Отправка сообщения админу"""
    text = format_client_data(data)
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=text, parse_mode="HTML")
