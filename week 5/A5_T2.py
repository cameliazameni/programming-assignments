def frame_word(p_word: str) -> None:
    """Print the word inside a decorative frame."""
    frame_line = "*" * (len(p_word) + 4)
    print(frame_line)
    print(f"* {p_word} *")
    print(frame_line)


def main() -> None:
    """Main function: handles program flow."""
    print("Program starting.\n")

    word = input("Insert word: ")
    print()

    frame_word(word)
    print()

    print("Program ending.")


if __name__ == "__main__":
    main()
