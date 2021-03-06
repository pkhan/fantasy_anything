import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker

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
