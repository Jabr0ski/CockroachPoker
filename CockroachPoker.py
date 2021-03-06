import random

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #self.uid = uid

class Judge(Card):
    pass
    
class Ingredient(Card):
    pass

Suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
Deck = []

def buildDeck():
    for s in Suits:
        for i in range (1, 14):
            c = Card(s, i)
            Deck.append(c)
    for c in Deck:
        print(c.name, c.value)

buildDeck()