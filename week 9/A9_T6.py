########################################################
# Task A9_T6
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

def showOptions() -> None:
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")


def insertLine(lines: list[str]) -> None:
    text = input("Insert text: ")
    lines.append(text)


def saveLines(lines: list[str]) -> None:
    if not lines:
        print("No lines to save.")
        return
    filename = input("Insert filename: ").strip()
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        print("Lines saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")


def main() -> None:
    print("Program starting.")
    lines: list[str] = []

    try:
        while True:
            showOptions()
            choice = input("Your choice: ").strip()

            if choice == "0":
                print("Exiting program.")
                break
            elif choice == "1":
                insertLine(lines)
            elif choice == "2":
                saveLines(lines)
            else:
                print("Invalid choice. Try again.")

    except KeyboardInterrupt:
        print("Keyboard interrupt and unsaved progress!")
        if lines:
            confirm = input("Save before quit(y/n)?: ").strip().lower()
            if confirm == "y":
                filename = input("Insert filename: ").strip()
                try:
                    with open(filename, "w", encoding="utf-8") as f:
                        for line in lines:
                            f.write(line + "\n")
                    print("Lines saved successfully!")
                except Exception as e:
                    print(f"Error saving file: {e}")
        # If no lines, or user said no, just exit gracefully

    print("Program ending.")


if __name__ == "__main__":
    main()
