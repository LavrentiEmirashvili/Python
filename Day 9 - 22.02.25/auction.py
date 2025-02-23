from art import logo
print(logo)
import os


highest_bid = 0
highest_bidder = ""
auction = {}
bidders = True
while bidders:
    print("Welcome to the secret auction program.")
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))
    bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
    auction[name] = bid
    if bidder == "yes":
        bidders = True
        os.system("cls")
    else:
        bidders = False
for auctioners in auction:
    if auction[auctioners] > highest_bid:
        highest_bid = auction[auctioners]
        highest_bidder = auctioners
print(highest_bid,highest_bidder)