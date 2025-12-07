def frameWord(PWord):
    """Print the word inside a decorative frame."""
    frame_line = "*" * (len(PWord) + 4)
    print(frame_line)
    print(f"* {PWord} *")
    print(frame_line)
    return None


def main():
    """Main function: handles program flow."""
    print("Program starting.")
    print()

    word = input("Insert word: ")
    print()

    frameWord(word)
    print()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
