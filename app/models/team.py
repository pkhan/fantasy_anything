from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship('League', backref='teams')
