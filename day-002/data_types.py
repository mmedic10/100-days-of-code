# Data Types

# String 

print("Hello"[0])

print("123" + "345")

# Integer

print(123+345)

print(123_456_789) # Python ignora los guiones bajos ya que esta es una ayuda visual para el usuario por ejemplo: 100.000.000 que es igual a 100000000

# Float

3.14159

# Boolean

True
False


# Cast Data Types

# String

num_char = len(input("What is your name?"))

print(type(num_char)) # Retorna el tipo de dato que se le entrega

new_num_char = str(num_char)

print("Your name has "+ new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))


################### Ejercicio: Suma de digitos ###################
 
# Suma de los digitos de un unico numero. Ejemplo: input -> 39 / output -> 12

two_digit_number = input()

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1 + num2)




# ---------------------------------------------------------

# Mathematical Operations in Python

3+5
7-4
3*2
6/3 # Toda division en Python devuelve un numero Flotante
2**2

# PEMDAS 
# ()
# **
# * /
# + -

print(3 *3 + 3 / 3 - 3)
print(3 * (3 + ((3 / 3) - 3)))


################### Ejercicio BMI ###################

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI = float(weight)/(float(height)**2)
print(int(BMI))


# ---------------------------------------------------------

# Print diferents data types

score = 0 
height = 1.8
isWinning =True

# f-string
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning} " )


# Ejercicio Life in Weeks

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
int_age = int(age)
weeks_left = (90-int_age)*52
print(f"You have {weeks_left} weeks left.")