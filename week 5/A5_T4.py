def askDimention(PPrompt: str) -> float:
    """Prompt the user for a dimention and return it as a float."""
    value = float(input(f"Insert {PPrompt}: "))
    return value


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    """Calculate and return the area of a rectangle."""
    area = PWidth * PHeight
    return area


def main():
    """Main function: handles program flow."""
    print("Program starting.")

    width = askDimention("width")
    height = askDimention("height")
    print()

    area = calcRectangleArea(width, height)
    print(f"Area is {area}²")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
