from Card import Card
import random

class Deck(object):
	deck_of_cards = []
	def __init__(self):
		cards_in_deck = 52
		index = 0
		while index < cards_in_deck:
			card_number = index % 13
			suit_number = int(index / 13)
			new_card = Card(number=card_number, suit=suit_number, image=None)
			self.deck_of_cards.append(new_card)
			index += 1

	def get_deck(self):
		return self.deck_of_cards

	def shuffle(self):
		return random.shuffle(self.deck_of_cards)

	def burn_card(self):
		self.deck_of_cards.pop(0)
		return self.deck_of_cards

	def deal(self):
		card = self.deck_of_cards[0]
		self.deck_of_cards.pop(0)
		return card
