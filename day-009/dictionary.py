programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", # siempre dejar una coma para seguir agregando datos
}

# Retrieving items from dicctionary
print(programming_dictionary["Bug"]) #-> Para acceder a un valor dentro del diccionario se le debe otorgar su KEY

# adding new items to dictionary 

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)


