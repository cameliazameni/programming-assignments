########################################################
# Task A9_T2
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

import sys


def main() -> None:
    print("Program starting.")
    try:
        code = int(input("Insert exit code(0-255): "))
    except ValueError:
        print("Invalid input. Exiting with code 1.")
        sys.exit(1)

    if 0 <= code <= 255:
        if code == 0:
            print("Clean exit")
        sys.exit(code)
    else:
        print("Exit code out of range. Exiting with code 1.")
        sys.exit(1)


if __name__ == "__main__":
    main()
