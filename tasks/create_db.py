import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from app.models.team import Base, Team

engine = sqlalchemy.create_engine("postgres://patrickconway@/postgres")

conn = engine.connect()

try:
    conn.execute("commit")
    conn.execute("drop database fantasy")
except sqlalchemy.exc.ProgrammingError:
    pass
conn.execute("commit")
conn.execute("create database fantasy")

conn.close()

engine = sqlalchemy.create_engine("postgres://patrickconway@/fantasy")
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

t = Team(name="awesome team")
session.add(t)
session.commit()
