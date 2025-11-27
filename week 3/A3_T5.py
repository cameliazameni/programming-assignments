print("program starting...\n")

print("Options:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("0. Exit")
choice = input("Choose an option: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = round((celsius * 1.8) + 32, 1)
    print(f"{(celsius, 1)} °C equals to {fahrenheit} °F")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = round((fahrenheit - 32) / 1.8, 1)
    print(f"{(fahrenheit, 1)} °F equals to {celsius} °C")


elif choice == "0":
    print("Exiting...")


else:
    print("Invalid choice! Please try again.\n")

print("Program ending")
