class Card(object):
	def _setNumber(self, number=None):
		self._number = number
	def _getNumber(self):
		return self._number

	def _setSuit(self, suit=None):
		self._suit = suit
	def _getSuit(self):
		return self._suit

	def _setImage(self, image=None):
		self._image = image
	def _getImage(self):
		return self._image

	def _setName(self, name=None):
		self._name = name
	def _getName(self):
		return self._name

	number = property(_getNumber, _setNumber)
	suit = property(_getSuit, _setSuit)
	image = property(_getImage, _setImage)
	name = property(_getName, _setName)
