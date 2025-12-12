########################################################
# Task A10_T5
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

def recursiveFactorial(PNum: int) -> int:
    """Calculate factorial recursively."""
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)


def main() -> None:
    print("Program starting.")
    try:
        num = int(input("Insert factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial {num}!")
            result = recursiveFactorial(num)
            print(f"{num} = {result}")
    except ValueError:
        print("Invalid input. Please insert an integer.")
    print("Program ending.")


if __name__ == "__main__":
    main()
