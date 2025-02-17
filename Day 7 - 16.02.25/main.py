import random
import artstage


word_list = ["aardvark", "baboon", "camel"]

end_of_game = False
chosen_word = random.choice(word_list)
length = len(chosen_word)
word = []
for i in range(length):
    word += "_"
print(chosen_word)
guesses = []
life = 6
def check():
    guess = input("Input a letter to guess\n").lower()
    

    for i in range(length):
        if guess in guesses:
            print('You have already guessed this letter')
            check()
            break
        if guess == chosen_word[i]:
            word[i] = guess
            correct_guess = True
    guesses.append(guess)
    return correct_guess  
    

   
while not end_of_game:
    if check():
        print("Correct Guess")
    else:
        life -= 1
    
    print(f"You have {life} lives left")
    print(artstage.stages[life])
    print("".join(word))
    if '_' not in word:
        end_of_game = True
        print("You won!")
        
else:
    print(f'You Lose, The word was: {chosen_word}')
