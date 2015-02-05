from models import *
import sqlalchemy

engine = sqlalchemy.create_engine("postgres://patrickconway@/fantasy")
Base.metadata.create_all(engine)
