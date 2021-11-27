import random
import time
import os
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
n= 12
def black():
        player_card=0
        dealer_card=0
        for i in range(0,3):
                player_points = random.randint(2,11)
                dealer_points = random.randint(2,11)
                time.sleep(2)
                print('Player Card Is :',player_points)
                print('Dealer Card Is :',dealer_points)
                player = player + player_points
                dealer = dealer + dealer_points
                print('Player Points:',player)
                print('Dealer Points :',dealer)

                if len(player_card) == 2:
                        if player_card[0].card_value == 11 and player_card[1].card_value == 11:
                                player_card[0].card_value = 1
                        player_score = 10

                        print("PLAYER CARDS: ")
                print(player_card, False)
        print("PLAYER SCORE = ", player_score)
 
        input()
