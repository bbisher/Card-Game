from Table import Table
from Deck import Deck
from Player import Player

table = Table()
deck = Deck()
player1 = Player()
player1.name = "Jon"
player1.money = 100
player2 = Player()
player2.name = "Beth"
player2.money = 100

deck.shuffle()

deck.burnCard()
card = deck.deal()
player1.addCard(card)
card = deck.deal()
player2.addCard(card)

card = deck.deal()
player1.addCard(card)
card = deck.deal()
player2.addCard(card)

print("")
print("Player 1 Cards:")
player1.checkCards()
table.add_to_pot(player1.bet(10))
print("")

print("Pot: ", table.get_pot())

print("")
print("Player 2 Cards:")
player2.checkCards()
print("")

#flop
deck.burnCard()
card = deck.deal()
table.cards_on_table.append(card)
print("Flop 1 Card: ", card.name)
card = deck.deal()
table.cards_on_table.append(card)
print("Flop 2 Card: ", card.name)
card = deck.deal()
table.cards_on_table.append(card)
print("Flop 3 Card: ", card.name)

#turn
deck.burnCard()
card = deck.deal()
table.cards_on_table.append(card)
print("Turn Card: ", card.name)

#river
deck.burnCard()
card = deck.deal()
table.cards_on_table.append(card)
print("River Card: ", card.name)
print("")
