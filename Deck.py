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
			new_card = Card()
			new_card.number = card_number
			new_card.suit = suit_number
			new_card.name = self.setPlayingCardName(card_number, suit_number)
			self.deck_of_cards.append(new_card)
			index += 1

	def get_deck(self):
		return self.deck_of_cards

	def shuffle(self):
		return random.shuffle(self.deck_of_cards)

	def burnCard(self):
		self.deck_of_cards.pop(0)
		return self.deck_of_cards

	def deal(self):
		card = self.deck_of_cards[0]
		self.deck_of_cards.pop(0)
		return card

	def setPlayingCardName(self, card_number, suit_number):
		name = None
		if(card_number == 0):
			name = "Ace of "
		elif(card_number == 10):
			name = "Jack of "
		elif(card_number == 11):
			name = "Queen of "
		elif(card_number == 12):
			name = "King of "
		else:
			name = str(card_number + 1) +" of "

		if(suit_number == 0):
			name += "Clubs"
		elif(suit_number == 1):
			name += "Diamonds"
		elif(suit_number == 2):
			name += "Hearts"
		elif(suit_number == 3):
			name += "Spades"
		return name
