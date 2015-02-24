from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", backref="players")

    league_id = Column(Integer, ForeignKey('leagues.id'))
    league = relationship("League", backref="players")

    parent_player_id = Column(Integer, ForeignKey('players.id'))
    parent = relationship("Player", remote_side=[id], backref="children")
