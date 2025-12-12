########################################################
# Task A10_T4
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

import sys


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    """Merge two sorted lists into PMerge."""
    i = j = 0
    while i < len(PLeft) and j < len(PRight):
        if PAsc:
            if PLeft[i] <= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
        else:
            if PLeft[i] >= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
    # Append remaining
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    """Sort list in-place using merge sort."""
    if len(PValues) <= 1:
        return

    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]

    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    PValues.clear()
    merge(left, right, PValues, PAsc)


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
    mergeSort(asc_values, True)
    print(f"Ascending '{filename}' -> {', '.join(map(str, asc_values))}")

    # Descending
    desc_values = values.copy()
    mergeSort(desc_values, False)
    print(f"Descending '{filename}' -> {', '.join(map(str, desc_values))}")

    print("Program ending.")


if __name__ == "__main__":
    main()
