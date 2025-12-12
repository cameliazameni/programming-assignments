########################################################
# Task A9_T7
# Developer Camelia Zameni
# Date 2025-12-12
########################################################

import sys
import os


def showHelp() -> None:
    print("Usage: python A9_T7.py <src_file> <dst_file>")
    print("Copies text file from <src_file> to <dst_file>.")


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    proceed = True

    # Check if destination exists
    if os.path.exists(PDstFile):
        answer = input(
            f'Destination file "{PDstFile}" exists. Overwrite (y/n)?: ').strip().lower()
        if answer != "y":
            print("Copy cancelled.")
            proceed = False

    if proceed:
        try:
            print(f'Source file "{PSrcFile}"')
            print(f'Destination file "{PDstFile}"')
            print(f'Copying file "{PSrcFile}" to "{PDstFile}".')

            with open(PSrcFile, "r", encoding="utf-8") as src, \
                    open(PDstFile, "w", encoding="utf-8") as dst:
                for line in src:
                    dst.write(line)

        except Exception as e:
            print(f"Error during copy: {e}")
            sys.exit(-1)


def main() -> None:
    print("Program starting.")

    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        showHelp()
        sys.exit(-1)

    srcFile = sys.argv[1]
    dstFile = sys.argv[2]

    copyFile(srcFile, dstFile)

    print("Program ending.")


if __name__ == "__main__":
    main()
