# IF Anidados
usuario_autenticado = True
usuario_admin = True
if usuario_autenticado:
    if usuario_admin:
        print("Tienes acceso a todo el sistema")
    else:
        print("Tienes acceso")
else:
    print("Acceso denegado")

# Ejemplo con elif
ocupacion = "Jubilado"
if ocupacion == "Estudiante":
    print("Tienes 50% de Descuento")
elif ocupacion == "Jubilado":
    print("Tienes 75% de Descuento")
elif ocupacion == "Desempleado":
    print("Tienes 10% de Descuento")

#Operadores and( & ) y or( | )
usuario_logeado = True
usuario_admin = True
if usuario_logeado and usuario_admin:
    print("Administrador")
elif usuario_logeado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesión")

# List Iteradores con IF
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP', 'Ruby', 'GO', 'C++']
print(lenguajes)
for lenguaje in lenguajes:
    if lenguaje == "Python":
        print(lenguaje.upper())
    else:
        print(lenguaje)