############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/
import random 
import os
from art import logo

play = "y"
while play == "y":
    os.system("cls")
    print(logo)

    userScore = 0
    dealerScore = 0

    userHand = []
    dealerHand = []

    def draw_card(player):
        global userScore, dealerScore
        if player == "user":
            drawnCard = random.choice(cards)
            userHand.append(drawnCard)
            if userScore > 10 and drawnCard == 11:
                userScore += 1
            else:
                userScore += drawnCard
        elif player == "dealer":
            drawnCard = random.choice(cards)
            dealerHand.append(drawnCard)
            if dealerScore > 10 and drawnCard == 11:
                dealerScore += 1
            else:
                dealerScore += drawnCard

    draw_card("user")
    draw_card("user")

    draw_card("dealer")
    draw_card("dealer")

    print(f"Your cards: {userHand}, current score: {userScore}\nComputer's first card: {dealerHand[0]}")

    if userScore == 21:
        print("BlackJack!!! You win")
    elif dealerScore == 21:
        print("Dealer drew BlackJack. You lose")
        break

    drawAnother = input("Type 'y' to get another card, type 'n' to pass: ")

    while drawAnother == "y":
        draw_card("user")
        print(f"Your cards: {userHand}, current score: {userScore}\nComputer's first card: {dealerHand[0]}")

        if userScore < 21 :
            drawAnother = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            break
    while dealerScore < 17 or (dealerScore == 17 and 11 in dealerHand):
        draw_card("dealer")

    print(f"Your final hand: {userHand}, final score: {userScore}\nComputer's final hand: {dealerHand}, final score: {dealerScore}")


    if userScore > 21:
        print("You went over. You lose  😭")
    elif dealerScore > 21:
        print("Dealer went over 21, You Win!")
    elif userScore > dealerScore:
        print("You Win!")
    elif userScore == dealerScore:
        print("Its a Draw!")
    else:
        print("You lose.")
    play = input("Do you want to play another game of BlackJack? Type 'y' or 'n':")


