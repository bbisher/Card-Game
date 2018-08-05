class Table(object):
    cards_on_table = []
    def __init__(self, pot=0, cards_on_table=[]):
        self.pot = pot
        self.cards_on_table = cards_on_table

    def get_pot(self):
        return self.pot

    def add_to_pot(self, amount):
        self.pot += amount
        return self.pot

    def remove_from_pot(self, amount):
        self.pot -= amount
        return self.pot

    def get_cards(self):
        return self.cards_on_table

    def add_card(self, card):
        return self.cards_on_table.append(card)

    def clear_cards(self):
        self.cards_on_table = []
