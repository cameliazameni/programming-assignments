def showOptions() -> None:
    """Show the available menu options."""
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice() -> int:
    """Prompt user to insert choice and return it as integer."""
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1


def main() -> None:
    """Main function: handles tally counter logic."""
    print("Program starting.")
    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
            print()
        elif choice == 2:
            count += 1
            print(f"Count increased to {count}")
            print()
        elif choice == 3:
            count = 0
            print("Count reset to 0")
            print()
        elif choice == 0:
            print("Exiting program.")
            break
        elif choice == -1:

            print()
        else:
            print("Unknown option!")
            print()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
