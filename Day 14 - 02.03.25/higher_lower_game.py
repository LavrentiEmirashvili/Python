import random
import os
import art
from game_data import data


def comparison(a, b):
    os.system("cls")
    print(art.logo)
    
    if score > 0:
        print(F"You're right! Current score: {score}.")

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

    print(art.vs)

    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")


def HLGame():
    global score
    score = 0
    a = random.choice(data)

    while True:
        b = random.choice(data)
        while b == a:
            b = random.choice(data)

        comparison(a,b)

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        

        if a["follower_count"] > b["follower_count"]:
            correctChoice = "a"
        elif a["follower_count"] == b["follower_count"]:
            correctChoice = "tie"
        else:
            correctChoice = "b"

        if choice == correctChoice or correctChoice == "tie":
            score += 1
            if "a" == correctChoice:
                a = a
            else:
                a = b
        else:
            os.system("cls")
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

HLGame()