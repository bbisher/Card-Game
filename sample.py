from Table import Table
from Deck import Deck
from Player import Player

table = Table()
deck = Deck()
players = []

player = Player()
player.name = "Jon"
player.money = 100
players.append(player)

player = Player()
player.name = "Beth"
player.money = 100
players.append(player)

deck.shuffle()

deck.burnCard()
for player in players:
    card = deck.deal()
    player.addCard(card)

for player in players:
    card = deck.deal()
    player.addCard(card)

print("")
for player in players:
    print(player.name + "'s Cards:")
    player.checkCards()
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
