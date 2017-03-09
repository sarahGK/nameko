from service import BlackJack
from api import Deck
from nameko.testing.services import worker_factory

def test_blackjack_service():
  service = worker_factory(BlackJack)

#  service.player.side_effect = "P"

  assert service.game.deck == Deck

  assert service.player.name == "player"
  assert service.player.hand == []

  assert service.dealer.name == "dealer"
  assert service.dealer.hand == []

  service.start.side_effect = "Game Start"
  service.hit.side_effect = "Player choose to hit"
  service.stick.side_effect == "Player choose to stick"

  service.start.assert_called_with()
  service.hit.assert_called_with()
  service.stick.assert_called_with()

if __name__ == '__main__':
  test_blackjack_service()
