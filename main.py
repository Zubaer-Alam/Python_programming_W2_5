
print("Program starting.\n")

Word = input("Insert a closed compound word: ")

Length = len(Word)
Reversed = Word[::-1]
LastCharacter = Word[-1]

print(f"The word you inserted is '{Word}' and in reverse it is '{Reversed}'.")
print(f"The inserted word length is {Length}")
print(f"Last character is '{LastCharacter}'")

print("\nTake substring from the inserted word by inserting...")

Start = int(input("1) Starting point: "))
End = int(input("2) Ending point: "))
Step = int(input("3) Step size: "))

Substring = Word[Start:End:Step]

print(f"\nThe word '{Word}' sliced to the defined substring is '{Substring}'.")
print("Program ending.")