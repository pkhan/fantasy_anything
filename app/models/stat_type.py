from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from base import Base

class StatType(Base):
    __tablename__ = 'stat_types'

    id = Column(Integer, primary_key=True)
    is_decimal = Column(Boolean, default=False)
    name = Column(String(250))

    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship('League', backref='stat_types')
