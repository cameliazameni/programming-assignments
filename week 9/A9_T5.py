########################################################
# Task A9_T5
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

def main() -> None:
    print("Program starting.")
    try:
        r = int(input("Insert red: "))
        g = int(input("Insert green: "))
        b = int(input("Insert blue: "))

        # Validate ranges
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise Exception("Value out of range")

        # Hex string
        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)

        print("RGB Details:")
        print(f"- Red {r}")
        print(f"- Green {g}")
        print(f"- Blue {b}")
        print(f"- Hex {hex_color}")

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")

    print("Program ending.")


if __name__ == "__main__":
    main()
