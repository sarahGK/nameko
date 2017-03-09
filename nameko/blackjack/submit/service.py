from api import Deck,PlayingDeck,User,checkDeck,start
from db import Base,Games,update,add

from nameko.rpc import rpc
from database_session import Session

class BlackJack(object):
  name = "blackjack"
  game = PlayingDeck()
  player = User(name="player")
  dealer = User(name="dealer")

  session = Session(Base)

  #start with game having a full deck of 52 cards
  @rpc
  def start(self):
    game = self.session.query(Games).order_by(Games.game_id.desc()).first()
    if  not game is None and game.result == 0:
      self.player.setHand(list(game.player_hand))
      self.dealer.setHand(list(game.dealer_hand))
      self.game.setDeck(list(game.deck))

    start(self.game,self.player,self.dealer)
    r1 = self.player.getResult(self.game) 
    r2 = self.dealer.getResult(self.game)

    if ( r1 == "" and r2 == ""):
      message = ""
      result = 0
    else:
      message = ' use start() to start a new game'
      result = 1

    if game is None or game.result == 1:
      add(self.session,self.player.hand,self.dealer.hand,self.game.deck,result)
    else:
      update(game,self.player.hand,self.dealer.hand,self.game.deck,result)

    self.session.commit()

    return "Player's hand: ", self.player.hand, "Dealer's hand: ", self.dealer.hand,'  ',r1+r2,message

  @rpc
  def hit(self):
    game = self.session.query(Games).order_by(Games.game_id.desc()).first()
    if not game is None and game.result == 0:
      self.player.setHand(list(game.player_hand))
      self.dealer.setHand(list(game.dealer_hand))
      self.game.setDeck(list(game.deck))

    checkDeck(self.game,self.player,self.dealer)
    self.player.drawCard(self.game)
    points = self.player.getPoints(self.game)
    result = 1
    if (points == 21):
      message = "Player wins! " + ','.join(self.player.hand) + '  use start() to start a game'
    elif (points > 21):
      message = "Player loses! " + ','.join(self.player.hand) + '  use start() to start a game'
    else:
      result = 0
      message = self.player.hand

    if game is None or game.result == 1:
      add(self.session,self.player.hand,self.dealer.hand,self.game.deck,result)
    else:
      update(game,self.player.hand,self.dealer.hand,self.game.deck,result)

    self.session.commit()


    return message


  @rpc
  def stick(self): 
    game = self.session.query(Games).order_by(Games.game_id.desc()).first()
    if  not game is None and game.result == 0:
      self.player.setHand(list(game.player_hand))
      self.dealer.setHand(list(game.dealer_hand))
      self.game.setDeck(list(game.deck))

    playerPoints = self.player.getPoints(self.game)
    dealerPoints = self.dealer.getPoints(self.game)

    if (dealerPoints > playerPoints): 
      message = " Dealer Wins! " + ','.join(self.dealer.hand) + '  use start() to start a game'  
    else:
      while(dealerPoints < 21):
        checkDeck(self.game,self.player,self.dealer)
        self.dealer.drawCard(game = self.game)
        dealerPoints = self.dealer.getPoints(self.game)
        if (dealerPoints > 21):
          message = " Player Wins!Dealer's hand: " + ','.join(self.dealer.hand) + '  use start() to start a game'
          break
        if (dealerPoints > playerPoints or dealerPoints == 21):
          message = " Dealer Wins! Dealer's hand: " + ','.join(self.dealer.hand) + '  use start() to start a game'
          break

    if game is None or game.result == 1:
      add(self.session,self.player.hand,self.dealer.hand,self.game.deck,1)
    else:
      update(game,self.player.hand,self.dealer.hand,self.game.deck,1)

    self.session.commit()



    return message,"Player's points:",playerPoints,"Dealer's points:",dealerPoints


