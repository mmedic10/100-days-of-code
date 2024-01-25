import random 

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

continue_game =True
hand = [rock,paper,scissors]
option = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors\n"))
if option >2 or option <0:
    continue_game = False
else:
    print(hand[option])
    machine_hand = int(random.randint(0,2))
    print(machine_hand)
    print(f"Computer choose: \n {hand[machine_hand]}")






if continue_game == True:
    if option == 0 :
        if machine_hand == 0:
            print("Draw")
        elif machine_hand == 1:
            print("You Lose")
        else:
            print("You Win!!")

    elif option == 1 :
        if machine_hand == 1:
            print("Draw")
        elif machine_hand == 2:
            print("You lose")
        else:
            print("You Win!!")

    else:
        if machine_hand == 2:
            print("Draw")
        elif machine_hand == 0:
            print("You lose")
        else:
            print("You Win!!")
else:
    print("You typed an invalid number, you lose!")
