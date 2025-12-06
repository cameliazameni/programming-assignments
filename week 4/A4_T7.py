print("Program starting.")
print("Check multiplicative persistence.")

n = int(input("Insert an integer: "))

steps = 0


while n >= 10:
    digits = [int(d) for d in str(n)]

    product = 1
    expression = ""

    for i, d in enumerate(digits):
        product = product * d
        if i == len(digits) - 1:
            expression = expression + str(d)
        else:
            expression = expression + str(d) + " * "
    print(expression, "=", product)

    n = product
    steps = steps + 1
print("No more steps.")
print(f"This program took {steps} step(s)")
print("Program ending.")
