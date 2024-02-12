import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if dificulty == 'easy':
    print("entre easy")
    attemps = 10
if dificulty == 'hard':
    print("entre hard")
    attemps = 5 

enigma = random.randint(1,100)

def adivinar(numero):
    print(f"You have {attemps} attempst remaining to guess the number.")
    if numero == enigma:
        print(f"You Win!! the number is {enigma}")
        return 0
    elif numero > enigma:
        print("Too high")
        
    else:
        print("Too low")
        
    
    if (attemps-1) == 0:
        print("You've run out of guesses, you lose")
        print(f"Psss, the correct answer is {enigma}")
        return attemps-1
    else:
        print("Guess again")
        return attemps-1


while attemps!= 0:
    print(f"You have {attemps} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attemps = adivinar(guess)


