class Table(object):
    def _setPot(self, pot=None):
        self._pot = pot

    def _getPot(self):
        return self._pot

    pot = property(_getPot, _setPot)

    def __init__(self):
        self.cards_on_table = []

    def addToPot(self, amount):
        self.pot += amount
        return self.pot

    def removeFromPot(self, amount):
        self.pot -= amount
        return self.pot

    def getCards(self):
        return self.cards_on_table

    def addCard(self, card):
        return self.cards_on_table.append(card)

    def clearCards(self):
        self.cards_on_table = []
