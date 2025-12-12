########################################################
# Task A9_T3
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

import sys


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f"## {filename} ##")
            for line in f:
                print(line.strip())
            print(f"## {filename} ##")
    except FileNotFoundError:
        print(f"Error! File '{filename}' does not exist.")
        sys.exit(1)

    print("Program ending.")


if __name__ == "__main__":
    main()
