def main():
    print("Program starting.")
    print("This program can read a file.")

    filename = input("Insert filename: ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f'#### START "{filename}" ####')
            for line in f:
                print(line.rstrip())
            print(f'\n#### END "{filename}" ####')
    except FileNotFoundError:
        print(f'File "{filename}" not found.')

    print("Program ending.")


if __name__ == "__main__":
    main()
