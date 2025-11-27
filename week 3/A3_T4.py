# my own work

print("Program starting.")
print("This is a program with simple menu where you can choose which operation the program performs. ")
name = input("Before the menu please insert your name: ")
print("Options: ")
print("1 - Print welcome message")
print("2 - Print the name backwards")
print("3 - Print the first character")
print("4 - Show the amount of characters in the name")
print("0 - Exit")

choice = input("Your choice: ")

if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print(f"Your name backward is {name[::-1]}")
elif choice == "3":
    print(f"The firat character in name {name} is {name[0]}")
elif choice == "4":
    print(f"There are {len(name)} characters in the name {name}")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown options.")

print("Program ending.")
