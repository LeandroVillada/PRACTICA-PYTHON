"""
    Funciones                                   Métodos
    mostrarNombre(nombre)                       nombre.upper()
"""
nombre = 'Leandro'

def mostrar_nombre(nombre = "Anonimous"):
    print(f"Hola {nombre}")

mostrar_nombre(nombre)
print(nombre.upper())
print(nombre.title())

# Crea una función que imprima un mensaje de bienvenida
def mensaje_bienvenida():
    print("Bienvenido a Python")
    
mensaje_bienvenida()

# Crea una funcion que tome un nombre de usuario y lo muestre como mensaje de bienvenida
def mensaje_bienvenida(nombre = "Anonimous"):
    print(f"Hola {nombre}")

mensaje_bienvenida("Nahuel")

# Crea una funcion que tome la última actividad que hiciste