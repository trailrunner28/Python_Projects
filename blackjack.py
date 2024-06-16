#!/usr/local/bin/python3


import random

card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11 }
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

def deal_card(deck):
    return deck.pop()

def calculate_total(hand):
    total= sum(card_values[card] for card in hand)
    #Adjust for aces
    for card in hand:
        if card == 'A' and total > 21:
            total -= 10
        return total
        
def player_turn(deck, player_hand):
    while True:
        player_choice = input( "Hit or Stand? ").lower()
        if player_choice == 'hit':
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("Your hand:", player_hand, "Total:", total)
            if total > 21:
                print("Bust! You lost.")
                return False
        elif player_choice == 'stand':
            return True

def dealers_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    return dealer_hand
    
while True:
    player_hand = [ deal_card(deck), deal_card(deck) ]
    dealer_hand = [ deal_card(deck), deal_card(deck) ]
    
    print("Your hand:", player_hand, "Total", calculate_total(player_hand))
    print("Dealer's hand:", dealer_hand[0])
    #Player's Turn
    if player_turn(deck, player_hand):
        dealer_hand = dealers_turn(deck, dealer_hand)
        print("Dealer's hand:", dealer_hand, "Total:", calculate_total(dealer_hand))
    #determine winner
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    if dealer_total > 21:
        print("You Win!!")
    if player_total <= 21 and player_total > dealer_total:
        print("You Win!!")
    elif dealer_total <= 21 and dealer_total > player_total:
        print("Dealer Wins!")
    if dealer_total == player_total:
        print("It's a Tie")
    #check if enough cards are available to play a hand and reshuffle if not
    if len(deck) < 10:
       deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
       random.shuffle(deck)
    # Check if player wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
print("Thanks For Playing!")


#setup a dictionary of the cards with the key and value
#setup the list of the deck times four

# BlackJack Plan
# 13 cards x4 =deck
# 
#
# dealer=
# player=
# import random
#
# deal two cards
# dealer shows second card
# count card value
#
# options hit or stay
#
# dealer shows second card
# if dealer is < 17: then
# dealer always hits
#
# if hand is < 11 : then
#     ace equals 11
# else:
#      ace equals 1
#
# compare totals
#
# if dealer amount = player amount: then
# push
# if dealer closer to or equal to 21:
# you lose
# if player is closer to or equal to 21:
# you win
# if player > 21 : then
# bust
# if player has [11,12,13] plus 14: then
# BLACKJACK!
