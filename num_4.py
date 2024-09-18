# START
num: int = int(input("enter a number:"))
account: int = 1
while not num % 7 == 0:
    account += 1
    num: int = int(input("enter a number again:"))
    if num % 11 == 0:
        break
else:
    pass
print(f"the number of input is: {account}")

# END