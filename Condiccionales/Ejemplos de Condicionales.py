"""
    == Igual a
    =! Distinto de
    >= Mayor o Igual a
    <= Menor o Igual a
    > Mayor a
    < Menor a
"""
balance = 500
print(balance)
if balance >=50:
    print("Puedes pagar")
else:
    print("No tienes saldo")

balance = 25
print(balance)
if balance >=50:
    print("Puedes pagar")
else:
    print("No tienes saldo")

#IF con Texto
lenguaje = "Python"
if lenguaje == "Python":
    print("El lenguaje seleccionado es Python")
else:
    print("El lenguaje seleccionado no es Python")

#Evaluar un Boolean
usuario_autenticado = False

if usuario_autenticado == False:
    print("No tienes acceso")
else:
    print("Tienes acceso")

usuario_autenticado = True

if usuario_autenticado:
    print("Tienes acceso")
else:
    print("No tienes acceso")

