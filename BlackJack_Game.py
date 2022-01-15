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

#create a class for a hand that is going to be held by the player or the computer
class Hand:
    #cretae a hand list that will containt the cards dealt to players
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    #when a card added to the hand, append the list, and adjust the value of the hand
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.name]
        if card.name == 'Ace':
            self.aces +=1

    #when value blow up, count Ace's value as 1 instead of 11
    def ace_adjust(self, card):
        if self.value >21 and self.aces:
            self.value -= 10
            self.aces -= 1

#create a chip class to keep track of chips for the player and how much was bet with each round of game
class Chips:
    #create the total chips varaible and bet chips variable
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    # add bet chips to total when win
    def win_bet(self):
        self.total += self.bet

    # deduct bet chips to total when lost
    def lose_bet(self):
        self.total -= self.bet



#Test Section
test_deck = Deck()
test_deck.shuffle()

card_dealt = test_deck.deal()
print(card_dealt)
test_hand = Hand()
test_hand.add_card(card_dealt)
print(test_hand.cards)



