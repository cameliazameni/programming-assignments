import svgwrite
from svgwrite.shapes import Rect, Circle


def drawSquare(PDwg: svgwrite.Drawing) -> None:
    print("Insert square")
    try:
        x = int(input("- Left edge position: "))
        y = int(input("- Top edge position: "))
        side = int(input("- Side length: "))
        fill = input("- Fill color: ")
        stroke = input("- Stroke color: ")
        PDwg.add(Rect(insert=(x, y),
                      size=(side, side),
                      fill=fill,
                      stroke=stroke))
    except ValueError:
        print("Invalid input for square. Skipping.")
    return None


def drawCircle(PDwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    try:
        cx = int(input("- Center x position: "))
        cy = int(input("- Center y position: "))
        r = int(input("- Radius: "))
        fill = input("- Fill color: ")
        stroke = input("- Stroke color: ")
        PDwg.add(Circle(center=(cx, cy),
                        r=r,
                        fill=fill,
                        stroke=stroke))
    except ValueError:
        print("Invalid input for circle. Skipping.")
    return None


def saveSvg(PDwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ").strip()
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        PDwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!")
    else:
        print("Save cancelled.")
    return None


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        showOptions()
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            saveSvg(dwg)
        else:
            print("Invalid choice. Try again.")

    print("Program ending.")


if __name__ == "__main__":
    main()
