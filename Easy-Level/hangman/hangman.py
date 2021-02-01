import random


print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
hidden_word = "-" * len(correct_word)
lives = 8
used_letters = ""

while True:
    print("\n" + hidden_word)
    player_letter = input("Input a letter:")
    if player_letter in used_letters:
        lives -= 1
        print("No improvements")
    elif player_letter in correct_word:
        new = ""
        for i in range(len(correct_word)):
            if player_letter == correct_word[i]:
                new += player_letter
            else:
                new += hidden_word[i]
        hidden_word = new
        used_letters += player_letter
    else:
        lives -= 1
        print("No such letter in the word")
    if hidden_word == correct_word:
        print(correct_word)
        print("You guessed the word!")
        print("You survived!")
        break
    if lives == 0:
        print("You are hanged!")
        break
