import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
hidden_word = correct_word[:3] + "-" * (len(correct_word) - 3)
player_word = input(f"Guess the word: {hidden_word}")
if player_word == correct_word:
    print("You survived!")
else:
    print("You are hanged!")
