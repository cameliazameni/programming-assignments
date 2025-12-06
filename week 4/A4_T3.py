print("Program starting.")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("Starting while-loop:")
i = start
while i <= stop:
    if i == stop:
        print(i)
    else:
        print(i, end=" ")
    i = i + 1
print("Program ending.")
