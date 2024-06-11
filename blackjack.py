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
        
def players_turn(deck, player_hand):
    while true:
        player_choice = input( "Hit or Stand? ").lower()
        if play_choice == 'hit':
            player_hand.append(deal_card(deck))
            total = calculate_total(player_hand)
            print("Your hand:", player_hand, "Total:", total)
            if total > 21:
                print("Bust! You lost.")
                return False
        elif player_choice == 'stand':
            return true

def dealers_turn(deck, dealer_hand):
    while calculate_total(dealer_hand(deck) < 17
        dealer_hand.append(deal_card(deck))
        return dealer_hand
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
