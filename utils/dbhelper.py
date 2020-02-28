import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = db.create_engine('mysql+pymysql://hinet:12345678@localhost:3306/shopping_bot')
Base.metadata.create_all(bind=engine)

# Session Object
Session = sessionmaker(bind=engine)
# Global DB Object
session = Session()
