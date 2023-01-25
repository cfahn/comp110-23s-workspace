"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730561750"

user_word: str = input("Enter a 5-character word: ")

if (len(user_word) < 5):
    print("Error: Word must contain 5 characters")
    quit()
if (len(user_word) > 5):
    print("Error: Word must contain 5 characters")
    quit()

user_letter: str = input("Enter a single character: ")

if (len(user_letter) > 1):
    print("Error: Character must be a single character.")
    quit()
if (len(user_letter) < 1):
    print("Error: Character must be a single character.")
    quit()

instances_found: int = 0

print("Searching for " + user_letter + " in " + user_word)

for int in range(len(user_word)):
    if user_letter == user_word[int]:
        print(user_letter + " found at index " + str(int))
        instances_found += 1

if (instances_found == 0):
    print("No instances of " + user_letter + " found in " + user_word)
if (instances_found == 1):
    print("1 instance of " + user_letter + " found in " + user_word)
if (instances_found >= 2):
    print(str(instances_found) + " instances of " + user_letter + " found in " + user_word)
