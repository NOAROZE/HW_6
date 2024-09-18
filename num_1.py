import random

name1: str = input("enter your name:")
name2: str = input("enter your name:")
name3: str = input("enter your name:")
name4: str = input("enter your name:")
winning_player: str = random.choice([name1, name2, name3, name4])
print(f"A winning player is: {winning_player}")
