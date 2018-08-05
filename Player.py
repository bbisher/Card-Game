class Player(object):
	def _setName(self, name=None):
		self._name = name
	def _getName(self):
		return self._name

	def _setMoney(self, money=0):
		self._money = money
	def _getMoney(self):
		return self._money

	def _setImage(self, image=""):
		self._image = image
	def _getImage(self):
		return self._image

	name = property(_getName, _setName)
	money = property(_getMoney, _setMoney)
	image = property(_getImage, _setImage)

	def __init__(self):
		self.cards = []

	def addCard(self, card):
		return self.cards.append(card)

	def removeCard(self, card):
		return self.cards.remove(card)

	def checkCards(self):
		for card in self.cards:
			print(card.name)

	def clearCards(self):
		cards = []

	def check(self):
		pass

	def fold(self):
		clearCards()

	def bet(self, amount):
		if(self.isBetValid(amount)):
			self.money -= amount
			return amount
		else:
			return 0

	def isBetValid(self, bet):
		if(bet > self.money):
			return False
		return True
