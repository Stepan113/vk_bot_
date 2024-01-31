from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from vk_bot.database.create_database import Question


def select_question(number_question: int) -> Question:
    engine = create_engine("sqlite:///database.db", echo=True)
    session = Session(engine, expire_on_commit=True)
    question = select(Question).where(Question.number_question == number_question)
    res = session.scalars(question).one()
    return res
