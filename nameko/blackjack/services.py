import random
from nameko.rpc import rpc,RpcProxy
from nameko_sqlalchemy import Session
from .models import Model,DeclaratvieBase

decks = ['A','A','A','A',
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
         'K','K','K','K',
        ]


def drawCards():

  if len(decks) > 0:
    random.seed()
    ind = random.randint(0,len(decks)-1)
    card = decks[ind]
    del decks[ind]
    return card
  
def getPoint(card):
  if card == 'A':
    pass
  elif card == 'J' or card == 'Q' or card == 'K':
    return 10
  else: 
    return int(card)

def getTotalPoint(hands):

  point = 0
  for card in hands:
    if not card == 'A':
      point = point + getPoint(card)
    else:
      point = point + 1

  if not 'A' in card:
    return point
  else:
    if point <= 11:
      return point + 10
    else:
      return point


