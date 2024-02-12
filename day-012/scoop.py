################### Scope ####################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope : 

# El Local Scope solo existe dentro de las funciones 

def drink_potion():
    potion_strenght = 2 
    print(potion_strenght)

drink_potion()
print(potion_strength) # -> Error de que la variable no esta definida

#Las variables creadas dentro de una funcion solo pueden ser utilizadas en la misma funcion

# Global Scope

player_health = 10 

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()
print(player_health)

# There is no Block Scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombie","Alien"]

    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy) # ->genera error por no estar definido

# Modifying Global Scope

enemies = 1 # Variable con alcance global 
 
def increase_enemies():
    #global enemies # debemos declarar que tenemos una variable de alcance global para poder modificarla
    # debemos evitar modificar variables globales por posibles errores a futuro
    print(f"enemies inside function: {enemies+1}")
    return enemies + 1 # Es mejor utilizar este tipo de sintaxis 

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants:

# Las variables globales constantes son aquellas que se definen y se esperan no cambiarlas nunca mas
# Generalmente se declaran para ingresarla en funciones y se declaran en mayuscula

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@medmatte"