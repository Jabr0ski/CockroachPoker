import random

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #self.uid = uid

class Player:
    def __init__(self, uid, hand, collection):
        self.uid = uid
        self.name = hand
        self.value = collection

Suits = ["Cockroach", "Stink Bug", "Spider", "Scorpion", "Fly", "Bat", "Rat", "Toad"]
Deck = []

def buildDeck():
    for s in Suits:
        for i in range (1, 9):
            c = Card(s, i)
            Deck.append(c)
    shuffle()
    #for c in Deck:
        #print(c.name, c.value)
        
def shuffle():
    random.shuffle(Deck)

def main():
    print("Cockroach Poker is a reverse set collection game that has nothing\
to do with poker – except that the game is all about bluffing, with cards that\
show cockroaches, rats and stink bugs. The goal is to force another player to\
collect 4 of any one type of critter, or to empty their hand.")
    buildDeck()
    playerCount = 0
    while(playerCount < 1 or playerCount > 5):
        try:
            playerCount = int(input('\nHow many AI opponents? Enter a number from 1 to 5: '))
        except:
            print("\nYou must enter a number.")
            continue
        if(playerCount < 1):
            print("\nYou'll have no opponents! Enter a number from 1 to 5.")
        if(playerCount > 5):
            print("\nYou can only have up to 5 opponents. Enter a number from 1 to 5.")
    
main()