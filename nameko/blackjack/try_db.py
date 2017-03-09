from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
class Players(Base):
    __tablename__ = 'players'
    name = Column(String, primary_key=True)
    hands = Column(String)
    dealer_hands = Column(String)
    deck = Column(String)
 
"""from sqlalchemy import create_engine
engine = create_engine('sqlite:///orm_in_detail.sqlite')
 
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)"""
 

