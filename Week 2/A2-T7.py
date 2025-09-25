print("program starting.")
temp = float(input("Insert fahrenheit: "))
Celsius = (temp - 32) / 1.8
Celsius = round(Celsius, 1)
print(f"{temp}°F is {Celsius}°C")
print("Program ending")