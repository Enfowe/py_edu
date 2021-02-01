import random


print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
hidden_word = "-" * len(correct_word)


for _ in range(8):
    print("\n" + hidden_word)
    player_letter = input("Input a letter:")
    if player_letter in correct_word:
        new = ""
        for i in range(len(correct_word)):
            if player_letter == correct_word[i]:
                new += player_letter
            else:
                new += hidden_word[i]
        hidden_word = new
    else:
        print("No such letter in the word")
        
print("""\nThanks for playing!
We'll see how well you did in the next stage""")
