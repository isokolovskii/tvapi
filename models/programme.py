from sqlalchemy import Integer, DateTime, Time, String, Column, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class Programme(Base):
    __tablename__ = 'programme'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    title_lang = Column(String(10))
    start = Column(DateTime, unique=True)
    end = Column(DateTime, unique=True)
    duration = Column(Time)
    description = Column(String)
    description_lang = Column(String(10))
    channel_id = Column(Integer, ForeignKey('channels.id'), unique=True)
    channels = relationship('Channels', cascade='delete')

    def __init__(self, id, title, title_lang, start, channel_id, description_lang, description, duration, end):
        self.id = id
        self.title = title
        self.title_lang = title_lang
        self.start = start
        self.end = end
        self.duration = duration
        self.description = description
        self.description_lang = description_lang
        self.channel_id = channel_id
