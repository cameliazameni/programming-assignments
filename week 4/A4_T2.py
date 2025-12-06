print("Program starting.")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("Starting for loop:")
for i in range(start, stop + 1):
    if i == stop:
        print(i)
    else:
        print(i, end=" ")
print("Program ending.")
