from sqlalchemy import Column, Integer, String

from models.base import Base


class Channels(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(255))
    lang = Column(String(10))
    icon = Column(String(255))

    def __init__(self, id, title, lang, icon):
        self.id = id
        self.title = title
        self.lang = lang
        self.icon = icon
