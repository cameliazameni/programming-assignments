
#         my own work
print("Program starting")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
main_choice = input("Your choice: ")
if main_choice == "1":
    print("Length options: ")
    print("1 - Meters to kilometers")
    print("2 - kilometers to meters")
    print("0 - Exit")

    length_choice = input("Your choice: ")
    if length_choice == "1":
        meters = float(input("Insert meters: "))
        kilometers = round(meters / 1000, 1)
        print(f"{meters} m is {kilometers} km")
    elif length_choice == "2":
        kilometers = float(input("Insert kilometers: "))
        meters = round(kilometers * 1000, 1)
        print(f"{kilometers} km is {meters} m")
    elif length_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")


elif main_choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams:")
    print("0 - Exit")
    weight_choice = input("Your choice: ")
    if weight_choice == "1":
        grams = float(input("Insert grams: "))
        pounds = round(grams * 0.00220462, 1)
        print(f"{grams} g is {pounds} lb")
    elif weight_choice == "2":
        pounds = float(input("Insert pounds: "))
        grams = round(pounds / 0.00220462, 1)
        print(f"{pounds} lb is {grams} g")
    elif weight_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")


elif main_choice == "0":
    print("Exiting...")

print("Program ending.")
