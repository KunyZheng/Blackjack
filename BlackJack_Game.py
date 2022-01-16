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
    def ace_adjust(self):
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

#cretae a function to take in player's bet
def take_bet(chips, player_name):
    while True:
        try:
            chips.bet = int(input('{}, please input how many chips you would like to bet in this round? '.format(player_name)))
        except ValueError:
            print('You must enter an integer value!')
        else:
            if chips.bet > chips.total:
                print('You can not excced the maximum chip on hand: '+ str(chips.total) +'!')
            else:
                break

#create a function to hit a card

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjust()

#create a function to determine whether hit or stand
def hit_or_stand(deck, hand):
  
    while True:
        h_or_s = input('Please enter h for hit and s for stand: ')

        if h_or_s[0].lower() == 'h':
            hit(deck, hand)

        elif h_or_s[0].lower() == 's':
            print("Player stands. Dealer's turn")
                
        else:
            print('Please enter h or s to hit or stand.')
            continue
        break
        




#Body of the Game Execution
#print('Welcome to the BlackJack Game!')
#player_name = input('Please enter your name: ')

#test_chips = Chips()
#take_bet(test_chips, player_name)

#test_deck = Deck()
#test_deck.shuffle()
#test_hand = Hand()
#hit_or_stand(test_deck, test_hand)
#print(test_hand.cards)
#print(test_hand.value)