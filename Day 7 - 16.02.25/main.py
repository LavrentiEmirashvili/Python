#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
length = len(chosen_word)
word = []
while length > 0:
    word.insert(1,"_")
    length -= 1
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Input a letter to guess\n").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print(word)
print(chosen_word)
for letter in chosen_word:
    if guess == letter:
        word[letter] = guess
    elif guess != letter:
        print("wrong")
    else:
        print("wrong input")
print(word)