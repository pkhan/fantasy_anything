from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Stat(Base):
    __tablename__ = 'stats'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)

    stat_type_id = Column(Integer, ForeignKey('stat_types.id'))
    stat_type = relationship("StatType")

    player_id = Column(Integer, ForeignKey('players.id'))
    player = relationship('Player', backref='stats')
