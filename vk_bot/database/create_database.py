from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session, Mapped, mapped_column, DeclarativeBase

engine = create_engine("sqlite:///database.db", echo=True)
session = Session(engine, expire_on_commit=True)


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "questions"
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str]
    link_on_image: Mapped[str]
    choose_questions: Mapped[str]
