########################################################
# Task A10_T6
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

import sys
import copy
import time
from typing import Callable


def readValues(PFilename: str, PValues: list[int]) -> None:
    """Read integers from file into PValues list."""
    PValues.clear()
    try:
        with open(PFilename, "r", encoding="utf-8") as f:
            for line in f:
                row = line.strip()
                if row != "":
                    PValues.append(int(row))
    except FileNotFoundError:
        print(f"Error! File '{PFilename}' not found.")
        sys.exit(1)
    return None


def bubbleSort(PNums: list[int]) -> list[int]:
    """Bubble sort implementation (ascending)."""
    n = len(PNums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
    return PNums


def quickSort(PNums: list[int]) -> list[int]:
    """Quick sort implementation (ascending)."""
    if len(PNums) <= 1:
        return PNums
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    return quickSort(left) + middle + quickSort(right)


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """Measure elapsed time in ns for sorting algorithm."""
    start = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    end = time.perf_counter_ns()
    return end - start


def showOptions() -> None:
    print("Options:")
    print("1 - Read dataset values")
    print("2 - Measure speeds")
    print("3 - Save results")
    print("0 - Exit")


def main() -> None:
    Values: list[int] = []
    Results: list[str] = []
    filename: str = ""

    print("Program starting.")

    while True:
        showOptions()
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":
            filename = input("Insert dataset filename: ").strip()
            readValues(filename, Values)

        elif choice == "2":
            if not Values:
                print("No dataset loaded. Please read dataset first.")
                continue
            print(f"Measured speeds for dataset '{filename}':")

            builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
            bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
            quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))

            print(f" - Built-in sorted {builtin_time} ns")
            print(f" - Bubble sort {bubble_time} ns")
            print(f" - Quick sort {quick_time} ns")

            Results.clear()
            Results.append(f"Measured speeds for dataset '{filename}':")
            Results.append(f" - Built-in sorted {builtin_time} ns")
            Results.append(f" - Bubble sort {bubble_time} ns")
            Results.append(f" - Quick sort {quick_time} ns")

        elif choice == "3":
            if not Results:
                print("No results to save. Please measure speeds first.")
                continue
            outname = input("Insert results filename: ").strip()
            try:
                with open(outname, "w", encoding="utf-8") as f:
                    for line in Results:
                        f.write(line + "\n")
                print(f"Results saved to '{outname}'.")
            except Exception as e:
                print(f"Error saving results: {e}")

        else:
            print("Invalid choice. Try again.")

    Values.clear()
    Results.clear()
    print("Program ending.")


if __name__ == "__main__":
    main()
