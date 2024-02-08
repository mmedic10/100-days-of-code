programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", # siempre dejar una coma para seguir agregando datos
}

# Retrieving items from dicctionary
print(programming_dictionary["Bug"]) #-> Para acceder a un valor dentro del diccionario se le debe otorgar su KEY

# adding new items to dictionary 
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)


#Create a empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A month in your computer."
print(programming_dictionary)

# Loop through a dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# Ejercicio: Grading program
    
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for key in student_scores:
    if student_scores[key]>=91:
        student_grades[key] = "Outstanding"
    elif student_scores[key]>=81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key]>=71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Belin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}

# Nesting a Dictionary in a Dictionary

travel_log = {
    "France" : {"cities_visited" : ["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visited" : ["Berlin","Hamburg","Stuttgart"],"total_visits": 5},
}

# Nesting a Dictionary in a List

travel_log = [
    {
        "country" : "France", 
        "cities_visited" : ["Paris","Lille","Dijon"],
          "total_visits": 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin","Hamburg","Stuttgart"],
        "total_visits": 5
    },
]

# Ejercicio: Dictionary in list

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country, visits, list_of_cities):
    new_input = {"country": country,"visits":visits,"cities":list_of_cities}
    travel_log.append(new_input)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

