from sqlalchemy import Column, Integer, String

from models.base import Base


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String(255))
    lang = Column(String(10))

    def __init__(self, id, title, lang):
        self.id = id
        self.title = title
        self.lang = lang
