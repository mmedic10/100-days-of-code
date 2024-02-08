############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear

def score_hand(hand):
    if sum(hand)==21 and len(hand)==2:
        return 0
    
    if 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    return sum(hand)


def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card  

def compare(user_score,computer_score):
    if user_score > 21 and computer_score> 21:
        return "You Lose"
    
    if user_score == computer_score:
        return "Draw"
    
    elif user_score == 0:
        return "You Win with a BlackJack"
    elif computer_score == 0:
        return "You Lose with a BlackJack"
    elif user_score>21:
        return "You Lose"
    elif computer_score > 21:
        return "You Win"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You Lose"
    

def blackjack_game():
    print(logo)
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())
    user_score = score_hand(user_cards)
    computer_score = score_hand(computer_cards)
    print(f"Your cards: {user_cards}, current score {user_score}")
    print(f"Computer First card: {computer_cards[0]}")
    continue_game = True


    while continue_game:
        if user_score == 0 or user_score>=21:
            continue_game = False  

        elif input("Type 'y' to get another card, type 'n' to pass") == 'y':
            user_cards.append(draw_card())
            user_score = score_hand(user_cards)
            print(f"Your cards: {user_cards}, current score {user_score}")
        else:
            continue_game = False


    while computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = score_hand(computer_cards)


    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    blackjack_game()
