import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")
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



    for j in range(word_length):
        print(placeholder[j], end="");

    if placeholder == chosenwordlist:
        correct = True
