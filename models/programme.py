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
    channel_id = Column(Integer, ForeignKey('channels.id'), unique=True)
    channels = relationship('Channels', cascade='delete')
