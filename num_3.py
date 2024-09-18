# START num_1
num: int = int(input("enter a number bigger than 0:"))
for i in range(1, num + 1, 1):
    for i in range(1, i + 1):
        print(i, end=" ")
    print()
for i in range(num + 1, 1, -1):
    for i in range(1, i - 1):
        print(i, end=" ")
    print()

# END

