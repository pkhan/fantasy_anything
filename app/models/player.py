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

    def score(self):
        my_score = 0
        for stat in self.stats:
            my_score += stat.score()

        for child in self.children:
            my_score += child.rollup_score()

    def rollup_score(self):
        my_score = 0
        for stat in self.stats:
            my_score += stat.rollup_score()
