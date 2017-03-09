from try_deck import PlayingDeck

if __name__ == '__main__':
  cards = []
  pc = PlayingDeck()
  for i in range(0,10):
    ch = pc.drawACard()
    cards.append(ch)
    print(ch)
    print('\n')

  p = pc.getTotalPoint(cards);
  print("the total points is :%d"%p);


