from Table import Table
from Deck import Deck
from Player import Player

table = Table()
deck = Deck()
player1 = Player(name="Jon", money=100, image="")
player2 = Player(name="Jane", money=100, image="")
players = [player1, player2]

deck.shuffle()

deck.burn_card()
card = deck.deal()
player1.cards.append(card)
card = deck.deal()
player2.cards.append(card)

card = deck.deal()
player1.cards.append(card)
card = deck.deal()
player2.cards.append(card)

print("")
print("Player 1 Cards:")
print(player1.cards[0].name)
print(player1.cards[1].name)
table.add_to_pot(player1.bet(10))
print("")

print(table.get_pot())

print("")
print("Player 2 Cards:")
print(player2.cards[0].name)
print(player2.cards[1].name)
print("")

#flop
deck.burn_card()
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
deck.burn_card()
card = deck.deal()
table.cards_on_table.append(card)
print("Turn Card: ", card.name)

#river
deck.burn_card()
card = deck.deal()
table.cards_on_table.append(card)
print("River Card: ", card.name)
print("")
