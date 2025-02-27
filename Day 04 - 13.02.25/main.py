import random
import art


# num = random.randint(0,1)

# #0 = Heads
# #1 = Tails

# if num == 1:
#     print("Tails")
# else:
#     print("Heads")



# states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states[4])


# names_str = input("give me everyones name seperated by a comma and a space")
# names = names_str.split(", ")
# payer = random.randint(0,len(names)-1)

# print(f"today bill will be payed by {names[payer]}")


# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# map = [row1,row2,row3]
# print(f'{row1}\n{row2}\n{row3}')
# position = input("Where do u want to put the treasure?\n")
# position_list = position.split(" ")
# column = int(position_list[1]) - 1
# row = int(position_list[0]) - 1
# print(row)
# map[row][column] = "x"

# print(f'{row1}\n{row2}\n{row3}')



#0 = rock
#1 = Paper
#2 = scissors

computerpick = random.randint(0, 2)
userinp = int(input("Choose rock(0) paper(1) or scissors(2):\n"))
if userinp == computerpick:
    print(f"You chose\n{art.rps[userinp]}\nComputer Chose\n{art.rps[computerpick]}\nIts a draw")
elif userinp == 0 and computerpick == 1 or userinp == 1 and computerpick == 2 or userinp == 2 and computerpick == 0:
    print(f"You chose\n{art.rps[userinp]}\nComputer Chose\n{art.rps[computerpick]}\nYou Lose")
else:
    print(f"You chose\n{art.rps[userinp]}\nComputer Chose\n{art.rps[computerpick]}\nYou WIn!")
input()