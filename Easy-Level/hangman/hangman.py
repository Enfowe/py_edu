import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
player_word = input("Guess the word:")
if player_word == correct_word:
    print("You survived!")
else:
    print("You are hanged!")
