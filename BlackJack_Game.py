#Lay out the type of suits and names of poker cards
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
names = ['Two', 'Three', 'Four', 'Five', 'Six','Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four': 4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen': 10, 'King':10, 'Ace':11}
import random

#create the card class for an individual poker card
class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __repr__(self):
        return self.name + ' of ' + self.suit

#create a deck class for an individual deck of cards
class Deck:
    #create a standard deck of cards
    deck = []
    def __init__(self):
        for suit in suits:
            for name in names:
               self.deck.append(Card(suit, name))

    def __repr__(self):
        deck_content = ''
        for card in self.deck:
            deck_content+= card.name + ' of '+card.suit+'\n'
        return deck_content


    #shuffle the sequence of the cards
    def shuffle(self):
        random.shuffle(self.deck)

    #deal a card from the deck
    def deal(self):
        card_drawn = self.deck.pop()
        return card_drawn



