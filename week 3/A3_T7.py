print("Program starting")
print("Testing decision structures")
value = int(input("Insert an integer: "))
print("Options: ")
print("1 _ In one multi-branched decision")
print("2 _ In multi independent if-statements")
print("0 _ Exit")
choice = int(input("Your choice: "))
if choice == 1:
    print("Using one multi-branched decision structure.")
    if value >= 400:
        value = value + 44
    elif value >= 200:
        value = value + 22
    elif value >= 100:
        value = value + 11
    print(f"Result is {value}")
elif choice == 2:
    print("Using multiple independent if-statements structure.")
    if value >= 400:
        value = value + 44
    if value >= 200:
        value = value + 22
    if value >= 100:
        value = value + 11
    print(f"Result is {value}")
elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")
print("Program ending.")
