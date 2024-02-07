# Randomization and Python List

import random 
#import my_module

random_integer = random.randint(1,10) # devuelve un numero entero aleatorio entre 1 y 10 
print(random_integer)

#print(my_module.pi)

random_float = random.random()
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is: {love_score}")

# Ejercicio : HEADS or TAILS

import random

coin = random.randint(0,1)
if coin == 0 :
    print("Tails")
else:
    print("Heads")

#######################################################
##################### LIST ############################
    
states_of_america = ["Delaware","Pennsylvani","Hola"]

print(states_of_america[0]) # Entre corchetes se coloca la posicion del elemento a devolver, empezando desde 0

print(states_of_america[-1]) # El numero negativo devuelve el elemento desde el final de la lista

states_of_america[2] = "New Jersey" # Al ya existir un elemento, es facil asignarle un nuevo valor
print(states_of_america[2])


states_of_america.append("Angeland") # Append agrega un unico elemento al final de la lista
states_of_america[-1]

states_of_america.extend(["Marcoland","Nicolad"]) # Extend agrega una lista de elementos al final de la lista original
print(states_of_america)

# Es posible tener lista dentro de listas



# Ejercicio Banker Roulette:

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

import random 

sel = random.randint(0,len(names)-1)
print(f"{names[sel]} is going to buy the meal today!")

# ------------------------------------------------------

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]


# Ejercicio

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "B2"

letra = position[0]
print(letra)
num = int(position[1])
print(num)
letras = ["A","B","C"]
pos_letra = letras.index(letra)
print(pos_letra)
map[num-1][pos_letra] = "X"

print(f"{line1}\n{line2}\n{line3}")



