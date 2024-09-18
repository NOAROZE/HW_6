# START
num: int = int(input("enter a number:"))
if num % 5 == 0 and num % 3 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Buzz")
elif num % 5 == 0:
    print("Fizz")
else:
    print("The number you entered is not divisible by 5 nor by 3")
# END
