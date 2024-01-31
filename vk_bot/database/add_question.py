from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from vk_bot.database.create_database import Question


def add_question(number_question: int,
                 question: str,
                 link_on_image: str,
                 choose_questions: str,
                 right_answer: str):
    question = Question(
        number_question=number_question,
        link_on_image=link_on_image,
        question=question,
        choose_questions=choose_questions,
        right_answer=right_answer
    )
    engine = create_engine("sqlite:///database.db", echo=True)
    session = Session(engine, expire_on_commit=True)
    session.add(question)
    session.commit()
    session.close()
