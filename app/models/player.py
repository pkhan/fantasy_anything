from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Player(Base):
    __tablename__ = 'players'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team")

    # parent_player_id = Column(Integer, ForeignKey('players.id'))
    
    # children = relationship("Player", backref="parent_player")
