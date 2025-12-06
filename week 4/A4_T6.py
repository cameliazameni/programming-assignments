print("Program starting.")
n = int(input("Insert a positive integer: "))
sequence = [n]
steps = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    sequence.append(n)
    steps = steps + 1
print(sequence)

print(f"total steps were {steps}.")

print("Program ending.")
