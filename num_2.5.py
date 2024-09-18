sum_temp: int = 0
for i in range(5):
    temp: int = int(input("Enter the temperature of a city you like:"))
    while temp < -50 or temp > 45:
        temp: int = int(input("Enter the temperature of a city you like again:"))
    sum_temp += temp
avg: float = sum_temp / 5
print(f"the average of temperature is: {avg}")
