import random
from asyncio import current_task

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


current_score = 0
comp_score = 0

picked_card = 0
playagain = True


while playagain:
    user_deck = []
    comp_deck = []
    current_score = 0
    comp_score = 0


    for i in range(2):
        user_deck.append(random.choice(cards))
        comp_deck.append(random.choice(cards))
    current_score=sum(user_deck)
    comp_score = sum(comp_deck)
    print("\n"*50)
    print(logo)
    print(f"Your cards: {user_deck}, current score = {current_score}")
    print(f"Computer's first card: {comp_deck[0]}")
    if input("Type 'y' to get another card, type 'n' to pass") == 'y':
        getanothercard = True
    else:
        getanothercard = False

    while getanothercard == True:

        picked_card = random.choice(cards)
        user_deck.append(picked_card)
        current_score = sum(user_deck)
        print(f"Your cards: {user_deck}, current score = {current_score}")
        print(f"Computer's first card: {comp_deck[0]}")
        if current_score > 21:
            getanothercard = False
        else:

            if input("Type 'y' to get another card, type 'n' to pass") == 'y':
                getanothercard = True
            else:
                getanothercard = False

    if current_score > 21:
        print(f"Your final hand: {user_deck}, final score: {current_score}")
        print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
        print(f"You went over, you lose.")
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'n':
            playagain = False

    elif current_score <= 21:
        while comp_score < 16:
            comp_deck.append(random.choice(cards))
            comp_score = sum(comp_deck)
        if comp_score < current_score:
            print(f"Your final hand: {user_deck}, final score: {current_score}")
            print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
            print("You WIN.")
            if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'n':
                playagain = False
        elif comp_score > 21:
            print(f"Your final hand: {user_deck}, final score: {current_score}")
            print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
            print(f"Opponent went over, you WIN.")
            if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'n':
                playagain = False


        elif comp_score > current_score:
            print(f"Your final hand: {user_deck}, final score: {current_score}")
            print(f"Computer's final hand: {comp_deck}, final score: {comp_score}")
            print("You LOSE.")
            if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'n':
                playagain = False
















