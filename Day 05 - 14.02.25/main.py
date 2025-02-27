# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# length = 0
# for i in student_heights:
#     length += 1

# avr = 0
# for n in range(0, length):
#     avr += student_heights[n]
# avr = (avr / (length))
# avr = round(avr)
# print(avr)

# student_scores = input("Input a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)



# highest = 0
# for score in student_scores:
#     if score > highest:
#         highest = score
# print(f"The highest score in the class is: {highest}")



# total = 0

# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)       

# EZZZZZZZZZZZZZZZZZZZZZZ


# for number in range(1, 101):
#     if number % 3 != 0 and number % 5 != 0:
#         print(number)
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")


#passgen

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_length = nr_letters + nr_symbols + nr_numbers
password = []

for letter in range(0, nr_letters):
    password.insert(random.randint(0,total_length),letters[random.randint(0,25)])
for number in range(0, nr_numbers):
    password.insert(random.randint(0,total_length),numbers[random.randint(0,9)])
for symbol in range(0, nr_symbols):
    password.insert(random.randint(0,total_length),symbols[random.randint(0,8)])
random.shuffle(password)
passwordstr = ''.join(password)
print(passwordstr)