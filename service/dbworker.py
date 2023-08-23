import datetime

from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Date, Text,\
    Boolean, Table, ForeignKey, SmallInteger
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, Mapped,\
    mapped_column
# from config import DATABASE


DATABASE = "sqlite:///sqlite.db"
engine = create_engine(DATABASE, echo=True)

class Base(DeclarativeBase):
    pass


class Client(Base):
    """Пользователь"""
    __tablename__ = 'client'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(12))  # TODO: Сделать уникальным поле
    bot_user_id: Mapped[int] = mapped_column(Integer, nullable=True)
    nickname: Mapped[str] = mapped_column(String(50), nullable=True)
    date: Mapped[str] = mapped_column(String(50), nullable=True)
    answer_point: Mapped[int] = mapped_column(Integer, nullable=True)
    answer_text: Mapped[str] = mapped_column(String(255), nullable=True)
    appointment: Mapped[bool] = mapped_column(Boolean, nullable=True)


    @property
    def serialize(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'bot_user_id': self.bot_user_id,
            'nickname': self.nickname,
            'answer_point': self.answer_point,
            'answer_text': self.answer_text,
            'appointment': self.appointment
        }


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()