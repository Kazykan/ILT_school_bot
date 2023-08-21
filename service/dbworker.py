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
    bot_user_id: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(12))  # TODO: Сделать уникальным поле


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()