import random
import artstage
import hangman_words


end_of_game = False
repeat = False
correct_guess = False

chosen_word = random.choice(hangman_words.word_list)
length = len(chosen_word)
word = []
for i in range(length):
    word += "_"
print(chosen_word)
guesses = []
life = 6

print(artstage.logo)
def check():
    global correct_guess
    global repeat
    
    repeat = False

    guess = input("Input a letter to guess\n").lower()
    if guess in guesses:
        print("You have already guessed this letter.")
        repeat = True
        return None
    guesses.append(guess)
    for i in range(length):
        if guess == chosen_word[i]:
            word[i] = guess
            correct_guess = True


while not end_of_game:
    correct_guess = False 
    check()
    if correct_guess:
        print("Correct Guess")
    elif correct_guess == False and repeat == False:
        life -= 1
        print("Wrong Guess")
    print(f"You have {life} lives left")
    print(artstage.stages[life])
    print("".join(word))
    if '_' not in word:
        end_of_game = True
        print("You won!")
    elif life == 0:
        end_of_game = True
        print(f"You lose! The word was: {chosen_word}")
