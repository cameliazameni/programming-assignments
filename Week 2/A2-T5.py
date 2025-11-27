
print("program starting")
compound = input("Insert a closed compound word: ")
reversed_compound = compound[::-1]
print(
    f"The word you inserted is '{compound}' and in reverse it is '{reversed_compound}'.")
print(f"The inserteed word length is {len(compound)}")
print(f"Last character is '{compound[-1]}'.")
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
substring = compound[start:end:step]
print(
    f"The word '{compound}' sliced to the defined substring is '{substring}'.")
print("Program ending.")
