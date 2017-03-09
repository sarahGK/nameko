import random

class PlayingDeck(object):
  deck = [ 'A','A','A','A',
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


  def drawACard(self):

    if len(self.deck) > 0:
      random.seed()
      ind = random.randint(0,len(self.deck)-1)
      card = self.deck[ind]
      del self.deck[ind]
      return card

    return "None"
    
  def getPoint(self,card):
    if card == 'A':
      return 1 
    elif card == 'J' or card == 'Q' or card == 'K':
      return 10
    elif card == "None":
      return 0
    else: 
      return int(card)

  def getTotalPoint(self,hands):

    point = 0
    for card in hands:
        point = point + self.getPoint(card)
      
    if not 'A' in hands:
      return point
    else:
      if point <= 11:
        return point + 10
      else:
        return point



"""if __name__ == '__main__':
  cards = []
  pc = PlayingDeck()
  for i in range(0,52):
    ch = pc.drawACard()
    print(ch)
    print('value:\n')
    print(pc.getPoint(ch))
    cards.append(ch)
    
  p = pc.getTotalPoint(cards);
  print("the total points is :%d"%p);"""






