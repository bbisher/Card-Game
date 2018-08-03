from Models.Card import Card
import random

class Deck:
	deck_of_cards = []

	def __init__(self, id):
		self.id = id
		cards_in_deck = 52
		deck_of_cards = []
		index = 0
		while index < cards_in_deck:
			card_number = index % 13
			suit_number = int(index / 13)
			new_card = Card(number=card_number, suit=suit_number, image=None)
			self.deck_of_cards.append(new_card)
			index += 1

	def shuffle(self):
		random.shuffle(self.deck_of_cards)

	def deal(self):
		card = self.deck_of_cards[0]
		self.deck_of_cards.pop(0)
		return card

	def burn_card(self):
		self.deck_of_cards.pop(0)

	def get_cards(self):
		return self.deck_of_cards
