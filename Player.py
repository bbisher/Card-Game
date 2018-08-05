class Player(object):
	cards = []
	def __init__(self, name, money, image):
		self.name = name
		self.money = money
		self.image = image

	def give_card(self, card):
		self.cards.append(card)

	def check_cards(self):
		for card in cards:
			print(self.cards.name)

	def bet(self, amount):
		if(self.is_bet_valid(amount)):
			self.money -= amount
			return amount
		else:
			return 0

	def is_bet_valid(self, bet):
		if(bet > self.money):
			return False
		return True
