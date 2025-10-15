def multiplicative_persistence(n):
    steps = 0
    print("\nCheck multiplicative persistence.")
    print(f"Insert an integer: {n}")

    while n >= 10:
        digits = [int(d) for d in str(n)]
        expression = " * ".join(str(d) for d in digits)
        result = 1
        for d in digits:
            result *= d
        print(f"{expression} = {result}")
        n = result
        steps += 1

    print("No more steps.")
    print(f"\nThis program took {steps} step(s)")


# Main program
print("Program starting.")
try:
    user_input = int(input("\nInsert an integer: "))
    if user_input < 0:
        print("Please enter a non-negative integer.")
    else:
        multiplicative_persistence(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
print("\nProgram ending.")
