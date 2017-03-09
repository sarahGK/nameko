from try_deck import PlayingDeck
import try_db as db

from nameko.rpc import rpc
from nameko_sqlalchemy import Session

class Dealer(object):
  name = "dealer"
  hands = []

  def drawCards(self,game):
    card = game.drawACard()
    self.hands.append(card)
    return card

class Player(object):
  name = "player"
  hands = []
  game = PlayingDeck()
  dealer = Dealer()

  session = Session(db.Base)
#  point = 0

#  def restart(self):
#    self.hands = []
#    self.game = PlayingDeck()
#    return "restart!"

  @rpc
  def login(self,name):
    player = self.session.query(players).filter(players.name == name)
    if player is None:
      player = Players(name=name,hands="",dealer_hands="",deck=''.join(self.PlayingDeck().deck))
      self.session.add(player)
      self.session.commit()
    else:
      self.hands = player.hands
      self.dealer.hands = player.dealer_hands
      self.game.deck = player.deck


  @rpc
  def hit(self):
    card = self.game.drawACard()
    self.hands.append(card)
    point = self.game.getTotalPoint(hands=self.hands) 

    if (point == 21):
      message = "Player win!" + ','.join(self.hands)
    elif (point > 21):
      message = "Player lose!" + ','.join(self.hands)
    else:
      return card,self.hands,point

    return message


  @rpc
  def stick(self):
    value = self.game.getTotalPoint(hands = self.hands)
    point = self.game.getTotalPoint(hands=self.dealer.hands)
    while(point < 21):
     self.dealer.drawCards(game = self.game)
     point = self.game.getTotalPoint(hands=self.dealer.hands)
     if (point > 21):
        return self.dealer.hands," Player Win!",value,point
     if (point > value):
       return self.dealer.hands,"Dealer win!",value,point
     if (point == 21):
       return self.dealer.hands,"Dealer win!",value,point


