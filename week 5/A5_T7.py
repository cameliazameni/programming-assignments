DELIMITER = ','


def collectWords() -> str:
    """Prompt user to insert words until empty input, return them joined by DELIMITER."""
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)

    return DELIMITER.join(words)


def analyseWords(PWords: str) -> None:
    """Analyse words: count words, characters, and average word length."""
    if not PWords:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return None

    word_list = PWords.split(DELIMITER)
    num_words = len(word_list)
    num_chars = sum(len(w) for w in word_list)
    avg_length = num_chars / num_words

    print(f"- {num_words} Words")
    print(f"- {num_chars} Characters")
    print("- {:.2f} Average word length".format(avg_length))
    return None


def main() -> None:
    """Main function: handles program flow."""
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
