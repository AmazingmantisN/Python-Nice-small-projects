
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

import random
word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list);
print(chosen_word);

placeholder = [];
word_length = len(chosen_word);
for position in range(word_length):
    placeholder.append("_");
print(placeholder)



display = []
chosenwordlist = []
for i in chosen_word:
    chosenwordlist.append(i);



correct = False
while (correct == False):
    print()
    guess = input("Guess a letter: ").lower()


    for i in range(word_length):
        if guess == chosenwordlist[i]:
            placeholder[i] = chosenwordlist[i];

    if guess not in chosenwordlist:
        lives -= 1;



    for j in range(word_length):
        print(placeholder[j], end="");

    print(stages[lives]);


    if lives == 0:
        print("You lose, the man died");
        correct = True;
    if placeholder == chosenwordlist:
        correct = True;
