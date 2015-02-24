from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class League(Base):
    __tablename__ = 'leagues'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))

    manager_id = Column(Integer, ForeignKey('teams.id', use_alter=True, name='fk_manager_id'))
    manager = relationship('Team', foreign_keys=manager_id, post_update=True)
