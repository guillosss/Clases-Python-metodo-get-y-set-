from clases.Personaje import Personaje
# creando instancia o creando objetos
personaje = Personaje("Juan", 800)

# ACCEDIENTO A METODO SET
personaje.nombre = "Catalina"
personaje.edad = 30
# ACCEDIENDO A LOS METODOS GET
print(personaje.nombre)
print(personaje.edad)
