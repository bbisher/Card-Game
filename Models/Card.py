class Card:	
	def __init__(self, number, suit, image):
		self.id = id
		self.number = number
		self.suit = suit
		self.image = image
		self.name = ""
		self.set_name()

	def set_name(self):
		if(self.number == 0):
			self.name = "Ace of "
		elif(self.number == 10):
			self.name = "Jack of "
		elif(self.number == 11):
			self.name = "Queen of "
		elif(self.number == 12):
			self.name = "King of "
		else:
			self.name = str(self.number + 1) +" of "

		if(self.suit == 0):
			self.name += "Clubs"
		elif(self.suit == 1):
			self.name += "Diamonds"
		elif(self.suit == 2):
			self.name += "Hearts"
		elif(self.suit == 3):
			self.name += "Spades"
