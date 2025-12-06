print("Program starting")
print("")
WordCount = 0
CharCount = 0
Word = input("Insert word (empty stops): ")
while Word != '':
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")
print("")
print("You inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} characters")
print("")
print("Program ending")
