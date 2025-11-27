#  my own work

print("Program starting.")
print("This is a program with simple menu where you can choose which operation the program performs.")
name = input("Before the menu please insert your name: ")
print("Options: ")
print("1 - Print welcome message")
print("0 - Exit")
choice = input("Your choice: ")

if choice == "1":
    print(f"Welcome, {name}!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option")

print("Program ending.")
