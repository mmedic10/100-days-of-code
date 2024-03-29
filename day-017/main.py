# Creacion de una clase
# Para crear una clase debemos seguir la siguiente estructura:
# class NombreClase:
# Un constructor es la parte de un objeto que nos permite especificar lo que ocurrir cuando se esta construyendo un objeto. Esto tambien se conoce como inicializar un objeto.
# Para inicializar un constructor debemos utilizar la funcion especial def __init__(self)
# Que tenga __init__ al principio y al final significa que es un metodo que el interprete de python conoce y que sabee que tiene una funcion especial
# self en la funcion init es el mismo objeto que se esta creando, todo lo que venga posterior sera los parametros que se pasaran
# Las clases tienen metodos y estos son los que realizan acciones de una cierta clase
# Todo metodo debe autollamarse (self)
class User: # forma de crear una clase
    def __init__(self,user_id,username): # Constructor
        # print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0 # Podemos poner valores por defecto
        self.following = 0

    def follow(self,user):
        self.followers += 1
        self.following += 1



# Podemos agregar atributos al objeto
# Atributo: variable asociada a un objeto
# Agregar atributos de esta manera es una mala practica ya que podemos equivocarnos y cambiar nombres
## user_1.id = "001"
## user_1.username = "angela"
#print(user_1.username)

user_1 = User("001","angela")
user_2 = User("002","marco")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)