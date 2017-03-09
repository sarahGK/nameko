from sqlalchemy import create_engine, Column, String, Integer,Sequence,SmallInteger
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///blackjack.sqlite',echo=True)
Base = declarative_base()

class Games(Base):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True,autoincrement=True) 
    player_hand = Column(String)
    dealer_hand = Column(String)
    deck = Column(String)
    result = Column(SmallInteger,nullable=False) # 1 means the game has finished while 0 means not

#    def __repr__(self):
#      return ("<Game(player's name='%s',player's hand='%s',dealer's hand='%s')>" %
#(self.player_name,self.player_hand,self.dealer_hand))

#Base.metadata.create_all(engine)

def update(game,phand,dhand,gdeck,result):
  if not game is None:
    game.player_hand = ''.join(phand)
    game.dealer_hand = ''.join(dhand)
    game.deck = ''.join(gdeck)
    game.result = result

def add(session,phand,dhand,gdeck,r):
  game = Games(player_hand = ''.join(phand),dealer_hand = ''.join(dhand),deck = ''.join(gdeck),result = r)
  session.add(game)


