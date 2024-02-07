# Simple Function
def greet():
    print("Hello Marco")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

# Function that allows for input 

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Marco")

# Argumento: Dato real que va a ser dado a la funcion cuando esta es invocada. ejemplo: buscar(123) -> 123 vendria a ser el argumento
# Parametro: nombre de los datos de la funcion. Usamos el parametro dentro de la funcion para referirnos a ella y esta almacena el valor del argumento.

#Functions with more than 1 input

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"what is it like in {location}?")

greet_with("Jack Bauer","Nowhere")
greet_with(location="Nowhere",name="Jack Bauer")


# ----------------------------------------------------------

# Ejercicio: PAINT AREA CALCULATOR

import math
def paint_calc(height,width,cover):
    number_of_cans = (height*width)/cover
    number_of_cans = math.ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5 
paint_calc(height=test_h, width=test_w, cover=coverage)

 
# Ejercicio: Prime numbers: 
def prime_checker(number):
    contador = 0
    for i in range(1,number+1):
        if number%i == 0:
            contador+=1
      
    if number == 1:
        print("It's not a prime number.")
    elif contador ==2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
n = int(input()) # Check this number
prime_checker(number=n)

