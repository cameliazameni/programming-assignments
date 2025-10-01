def celsius_to_fahrenheit(c):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        c (float): Temperature in Celsius.
    Returns:
        float: Temperature in Fahrenheit.
    """
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    """
    Convert Fahrenheit temperature to Celsius.

    Args:
        f (float): Temperature in Fahrenheit.
    Returns:
        float: Temperature in Celsius.
    """
    return (f - 32) / 1.8


def main():
    """
    Main function to run the temperature converter program.
    Provides options to convert Celsius <-> Fahrenheit or exit.
    """
    print("program starting...\n")
    while True:
        print("Options:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            c = float(input("Enter temperature in Celsius: "))
            f = celsius_to_fahrenheit(c)
            print(f"{round(f, 1)} °F\n")

        elif choice == "2":
            f = float(input("Enter temperature in Fahrenheit: "))
            c = fahrenheit_to_celsius(f)
            print(f"{round(c, 1)} °C\n")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.\n")

            if __name__ == "__main__":
                main()
