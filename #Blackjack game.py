#Blackjack game

import random
import time

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for value in range(1,14):
                if value == 1:
                    value = "Ace"
                elif value == 11:
                    value = "Jack"
                elif value == 12:
                    value = "Queen"
                elif value == 13:
                    value = "King"
                self.cards.append(Card(suits, value))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
                    

    def show(self):
        for cards in self.cards:
            cards.show()
    
    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0

    def player_draw(self, deck):
        self.hand.append(deck.draw_card())
        

    def show_hand(self):
        for card in self.hand:
            card.show()

    def dealer_show(self):
        self.hand[1].show()

    def hand_total_count(self): 
        for numbers in self.hand:
            if numbers.val == "Jack" or numbers.val == "Queen" or numbers.val == "King":
                numbers.val = 10
                self.hand_value += numbers.val
            elif numbers.val == "Ace":
                numbers.val = 11
                self.hand_value += numbers.val
                numbers.val = "Ace"
                if self.hand_value > 21:
                    self.hand_value -= 10
            else:
                self.hand_value += numbers.val
        return self.hand_value

    def add_card_count(self):
        if  self.hand[-1].val == "Jack" or self.hand[-1].val == "Queen" or self.hand[-1].val == "King":
            self.hand[-1].val = 10
            self.hand_value += self.hand[-1].val
        elif self.hand[-1].val == "Ace":
            self.hand[-1].val = 11
            self.hand_value += self.hand[-1].val
            #self.hand[-1].val = "Ace"
            if self.hand_value > 21:
                self.hand_value -= 10
        else:
            self.hand_value += self.hand[-1].val
        return self.hand_value




'''
player_balance = 1000
'''
dealer = "Dealer"
dealer = Player(dealer)

card_deck = Deck()
card_deck.shuffle()

player_name = input("What is your name? ")

player_name = Player(player_name)

for i in range(2):
    player_name.player_draw(card_deck)
    dealer.player_draw(card_deck)

print("Your hand")
player_name.show_hand()
hand_total = player_name.hand_total_count()
print("-----------------------------------------------------------------")
print("Dealer's hand")
dealer.dealer_show()
dealer_total = dealer.hand_total_count()

while True:
    if hand_total == 21:
        print("Blackjack! Dealer's turn")
        break
    elif hand_total < 21:
        hit_choice = input("Would you like a hit? ")
        if hit_choice == "yes":
            player_name.player_draw(card_deck)
            player_name.show_hand()
            hand_total = player_name.add_card_count()
            #print(hand_total)
        elif hit_choice == "no":
            #hand_total = player_name.hand_total_count()
            print(f"Your hand's total is: {hand_total}")
            break
    elif hand_total > 21:
        print(hand_total)
        print("You busted :(")
        print("Dealer wins")
        break

if hand_total <= 21:
    print("Dealer's hand")
    dealer.show_hand()
    time.sleep(1)
    while True:
        if dealer_total == 21:
            break
        elif dealer_total < 17:
            print("Dealer hits")
            dealer.player_draw(card_deck)
            dealer.show_hand()
            dealer_total = dealer.add_card_count()
            time.sleep(1)
        elif dealer_total >= 17:
            break
    print(f"Dealer's total is: {dealer_total}")

if dealer_total == hand_total:
    print("Tie, no one wins")
elif hand_total <=21 and hand_total > dealer_total:
    print("You win, congrats!")
elif dealer_total > hand_total:
    print("Dealer wins, better luck next time")
    






