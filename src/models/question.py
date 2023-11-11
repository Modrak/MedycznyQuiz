from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('sections.id'))
    question_text = Column(String)
    ans_1 = Column(String)
    ans_2 = Column(String)
    ans_3 = Column(String)
    ans_4 = Column(String)
    ans_5 = Column(String)
    hint_1 = Column(String)
    hint_2 = Column(String)
    hint_3 = Column(String)
    hint_4 = Column(String)
    hint_5 = Column(String)
    right_answer_index = Column(Integer)

    section = relationship('Section', backref='questions')
