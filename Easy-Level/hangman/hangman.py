# JetBrains Academy
# Project: Hangman
# Stage 8/8

import random
import string

print("H A N G M A N")


def game_way():
    if_game = None
    while if_game not in ["play", "exit"]:
        if_game = input('Type "play" to play the game, "exit" to quit:')
    return if_game == "play"


words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
hidden_word = "-" * len(correct_word)
lives = 8
used_letters = ""

while game_way():
    while True:
        print("\n" + hidden_word)
        player_letter = input("Input a letter:")
        if len(player_letter) != 1:
            print("You should input a single letter")
        elif player_letter in used_letters:
            print("You already typed this letter")
        elif player_letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
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
            used_letters += player_letter
        if hidden_word == correct_word:
            print(f"You guessed the word {correct_word}!")
            print("You survived!")
            break
        if lives == 0:
            print("You are hanged!")
            break
    if lives == 0:
        break
