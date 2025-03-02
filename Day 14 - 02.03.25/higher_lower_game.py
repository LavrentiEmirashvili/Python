import random
import os
import art
from game_data import data

print(art.logo)

a = random.choice(data)
b = random.choice(data)

print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}")

print(art.vs)

print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}")

choice = input("Who has more followers? Type 'A' or 'B': ")