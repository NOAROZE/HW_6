import random

num: int = random.randint(0, 100)
print(num)
guess: int = int(input("enter a number:"))
account: int = 1
while guess != num:
    if guess > num:
        print("your number is too big")
    elif guess < num:
        print("your number is too small")
    guess: int = int(input("enter a number again:"))
    account += 1
else:
    print("bingo")
    print(f"The number of guesses is: {account}")
    pass
