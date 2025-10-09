

print("program starting.")
print("")
Feed = input("Insert starting value: ")
start = int(Feed)
Feed = input("Insert stopping value: ")
stop = int(Feed) + 1
print("")
print("starting while-loop:")
current = start
while current != stop:
    if (current == (stop)):
        print(current)
    else:
        print(current, end=' ')
        current += 1
        print("")
print("program ending.")
