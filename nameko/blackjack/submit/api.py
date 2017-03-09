import random

Deck = [ 'A','A','A','A',
         '2','2','2','2',
         '3','3','3','3',
         '4','4','4','4',
         '5','5','5','5',
         '6','6','6','6',
         '7','7','7','7',
         '8','8','8','8',
         '9','9','9','9',
         '10','10','10','10',
         'J','J','J','J',
         'Q','Q','Q','Q',
         'K','K','K','K'
        ]

class PlayingDeck(object):
  def __init__(self):
    self.deck = Deck

  def setDeck(self,cards):
    self.deck = cards

  def drawCard(self):
    if len(self.deck) > 0:
      random.seed()
      ind = random.randint(0,len(self.deck)-1)
      card = self.deck[ind]
      del self.deck[ind]
      return card

    return "None"
    
  def getPoints(self,card):
    if card == 'A':
      return 1 
    elif card == 'J' or card == 'Q' or card == 'K':
      return 10
    elif card == "None":
      return 0
    else: 
      return int(card)

  def getTotalPoints(self,hand):
    points = 0
    for card in hand:
        points = points + self.getPoints(card)
      
    if 'A' in hand and points <= 11:
        return points + 10
    return points

class User(object):
  def __init__(self,name):
    self.name = name
    self.hand = []

  def start(self,game): 
    self.setHand(cards=[])
    self.drawCard(game)
    self.drawCard(game)
    return self.name,"All started!"


  def setHand(self,cards):
    self.hand = cards

  def drawCard(self,game):
    card = game.drawCard()
    self.hand.append(card)
    return card

  def getPoints(self,game):
    point = game.getTotalPoints(self.hand)
    return point

  def getResult(self,game):
    if self.getPoints(game) == 21:
      message = self.name + "wins!" + ','.join(self.hand)
    elif self.getPoints(game) > 21:
      message = self.name + "loses!" + ','.join(self.hand)
    else:
      message = ""

    return message


def checkDeck(game,player,dealer):
  if len(game.deck) == 0:
      game.resetDeck(Deck-player.hand-dealer.hand)

def start(game,player,dealer):
   if len(game.deck) < 4:
      game.resetDeck(Deck-player.hand-dealer.hand)

   player.start(game)
   dealer.start(game)

   return "All restarted!"


