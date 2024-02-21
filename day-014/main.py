from game_data import data
import random
import art
from replit import clear

continuar = True
print(art.logo)
score = 0



compare_a = data[random.randint(0,len(data)-1)]

while continuar==True:
    compare_b = data[random.randint(0,len(data)-1)]
    if score != 0:
        print(art.logo)
        print(f"You're right! Your current score: {score}")
    print (f'Compare A: {compare_a["name"]}, a {compare_a["description"]}, from {compare_a["country"]}')
    print(art.vs)
    print (f'Compare B: {compare_b["name"]}, a {compare_b["description"]}, from {compare_b["country"]}')
    answer = input("Who has more followers? Type 'A' or 'B' ").upper()

    if  answer == "A":
        if compare_a["follower_count"]>=compare_b["follower_count"]:
            score+=1
        else:
            continuar = False
    elif answer == "B":
        if compare_b["follower_count"]>compare_a["follower_count"]:
            score+=1
            compare_a = compare_b
        else:
            continuar = False
    clear()

print(f"Sorry, that's wrong. Final score: {score}")