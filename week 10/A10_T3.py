########################################################
# Task A10_T3
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

import sys


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    """Sort list in-place using bubble sort."""
    n = len(PValues)
    for i in range(n - 1):  # outer loop for passes
        for j in range(n - i - 1):  # inner loop for comparisons
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
    return None


def readValues(filename: str) -> list[int]:
    values: list[int] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                row = line.strip()
                if row != "":
                    values.append(int(row))
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
        sys.exit(1)
    return values


def main() -> None:
    print("Program starting.")

    # filename from CLI or prompt
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input("Insert filename: ").strip()

    values = readValues(filename)

    # Raw
    print(f"Raw '{filename}' -> {', '.join(map(str, values))}")

    # Ascending
    asc_values = values.copy()
    bubbleSort(asc_values, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_values))}")

    # Descending
    desc_values = values.copy()
    bubbleSort(desc_values, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_values))}")

    print("Program ending.")


if __name__ == "__main__":
    main()
