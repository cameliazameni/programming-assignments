########################################################
# Task A10_T1
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

def readFile(filename: str) -> list[str]:
    values: list[str] = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                row = line.strip()
                if row != "":
                    values.append(row)
    except FileNotFoundError:
        print(f"Error! File '{filename}' not found.")
    return values


def displayVertically(values: list[str]) -> None:
    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")


def displayHorizontally(values: list[str]) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()
    values = readFile(filename)

    if values:
        displayVertically(values)
        displayHorizontally(values)

    print("Program ending.")


if __name__ == "__main__":
    main()
