import random
import tkinter as tk

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        #self.uid = uid

class Player:
    def __init__(self, uid, hand, collection, viewed):
        self.uid = uid
        self.hand = hand
        self.collection = collection
        self.viewed = viewed

Suits = ["Cockroach", "Stink Bug", "Spider", "Scorpion", "Fly", "Bat", "Rat", "Toad"]
Deck = []
Players = []

def buildDeck():
    for s in Suits:
        for i in range (1, 9):
            c = Card(s, i)
            Deck.append(c)
    shuffle()

#shuffle the deck
def shuffle():
    random.shuffle(Deck)

#deal cards out to participating player and AIs
def deal():
    firstPlayerIndex = random.randint(1, len(Players))
    currPlayerIndex = firstPlayerIndex
    while len(Deck) > 0:
        currPlayer = findPlayer(currPlayerIndex % len(Players)+1)
        currPlayer.hand.append(Deck.pop())
        currPlayerIndex += 1
    firstPlayerIndex = (firstPlayerIndex % len(Players)+1)
    print("\nPlayer", firstPlayerIndex, "starts!")
    return firstPlayerIndex


#pid = player ID passed to find
def findPlayer(pid):
    for p in Players:
        if(p.uid == pid):
            return p

def gameLoop():
    currentPlayerIndex = deal()
    currPlayer = findPlayer(currentPlayerIndex)
    window = tk.Tk()
    windowTitle = tk.Label("The Current Game State")
    currPlayer = tk.Label("")
    currOpps = tk.Label("")
    for p in Players:
        if(p.uid == 1):
            currPlayer = "You currently have"
        else:
            currOpps += "\nPlayer" + p.uid + "has"

def main():
    #window = tk.Tk()
    #mainTitle = tk.Label(text="Cockroach Poker")
    #about = tk.Label(text="Cockroach Poker is a reverse set collection game that\
#has nothing to do with\n poker – except that the game is all about bluffing, with\
#cards that show \ncockroaches, rats and stink bugs. The goal is to force another\
#player to\n collect 4 of any one type of critter, or to empty their hand.")
    #entry = tk.Entry(width=50)
    #mainTitle.pack()
    #about.pack()
    #window.mainloop()
    print("Cockroach Poker is a reverse set collection game that has nothing\
to do with poker – except that the game is all about bluffing, with cards that\
show cockroaches, rats and stink bugs. The goal is to force another player to\
collect 4 of any one type of critter, or to empty their hand.")
    buildDeck()
    opponentCount = 0
    while(opponentCount < 1 or opponentCount > 5):
        try:
            opponentCount = int(input('\nHow many AI opponents? Enter a number from 1 to 5: '))
        except:
            print("\nYou must enter a number.")
            continue
        if(opponentCount < 1):
            print("\nYou'll have no opponents! Enter a number from 1 to 5.")
        if(opponentCount > 5):
            print("\nYou can only have up to 5 opponents. Enter a number from 1 to 5.")
    
    for i in range (1, opponentCount + 2):
        p = Player(i, [], [], False)
        Players.append(p)
    
    print("\nYou are player 1 and you have", opponentCount, "opponents.")
    
    gameLoop()

main()