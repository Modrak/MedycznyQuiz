from sqlalchemy import Column, Integer, String

from .base import Base


class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True)
    name = Column(String)
