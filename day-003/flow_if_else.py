# Condicionales

print("Welcome to the rollercoaster!")

height = int(input("What is your hight in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    
    if age <12:
       print("Child tickets are $5.")
       bill = 5
    
    elif age<=18:
       print("Youth tickets are $7.")
       bill = 7
    elif age >= 45 and age <=55:
       print("Everything is goint to be ok. HAve a free ride on us!")

    else:
       print("Adult tickets are $12.")
       bill = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")  
    if wants_photo == "Y":
       # Add $3 to their bill
       bill+=3
       
    print(f"Your final bill is ${bill}")


else:
    print("Sorry, you have to grow taller before you can ride.")

# Comparation Operators 
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to
    
# Ejercicio: Par o impar
    
number = int(input())

if number % 2 != 0:
  print("This is an odd number.")
else:
  print("This is an even number.")

# Ejercicio Año biciesto 
  
# Which year do you want to check?
year = int(input())

if year%4 == 0:
    if year%100 == 0:
        if year%400 ==0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Ejercicio BMI 2.0
  
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

bmi = weight/(height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Ejercicio Pizza Order Practice

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if add_pepperoni == "Y":
    if size != "S":
        bill+=3
    else:
        bill+=2
if extra_cheese == "Y":
    bill+=1

print(f"Your final bill is: ${bill}.")

# Logical Operators
# and
# or
# not

# Ejercicio Love Calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

low_name1 = name1.lower()
low_name2 = name2.lower()
full_names = low_name1 + low_name2
score1 = 0
score2 = 0

score1 += full_names.count("t")
score1 += full_names.count("r")
score1 += full_names.count("u")
score1 += full_names.count("e")

score2 += full_names.count("l")
score2 += full_names.count("o")
score2 += full_names.count("v")
score2 += full_names.count("e")

final_score = int(str(score1)+str(score2))

if final_score <10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >=40 and final_score <=50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")