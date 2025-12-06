print("Program starting.")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
violation = False
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    violation = True
if not (start <= inspect <= stop):
    print("Inspection value must be within the range of start and stop.")
    violation = True
if violation:
    print("Program ending.")
else:
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspect:
            break
        print(i, end=" ")
    print()
    print("Second loop - inspection with continue:")
    for i in range(start, stop):
        if i == inspect:
            continue
        print(i, end=" ")
    print()
    print("Program ending.")
