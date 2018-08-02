from Models.Deck import Deck

deck = Deck()
#deck.shuffle()
cards = deck.get_cards()

for card in cards:
    print("Name: ", card.name)    
    print("")
