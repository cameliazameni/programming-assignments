def collatz_sequence(n):
    steps = 0
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps


print("Program starting.")
try:
    num = int(input("Insert a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        sequence, steps = collatz_sequence(num)
        print(" -> ".join(map(str, sequence)))
        print(f"Sequence had {steps} total steps.")
except ValueError:
    print("Invalid input. Please enter an integer.")
print("Program ending.")
