import random
from art import logo

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1,100)

difficulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5


while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("The guess is correct!")
        break
    elif guess > number:
        print("Too high.\nGuess again.")
        attempts -= 1
    elif guess < number:
        print("Too low.\nGuess again.")
        attempts -= 1