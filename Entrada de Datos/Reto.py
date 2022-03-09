# Realiza un examen con 3 preguntas que tu desees, el usuario deberá Responder "SI" o "NO" y al final otorgarle una calificación (La calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)

Puntos = 0
print(f"Puntos: {Puntos}")

Respuesta_1 = input("Gonzalo se la come?: ")
if Respuesta_1 == "NO":
    Puntos = Puntos + 1
print(f"Puntos: {Puntos}")

Respuesta_2 = input("Juan Cruz gusta de Nazareno?: ")
if Respuesta_2 == "SI":
    Puntos = Puntos + 1
print(f"Puntos: {Puntos}")

Respuesta_3 = input("Alvaro le presume a Maxi?: ") 
if Respuesta_3 == "SI":
    Puntos = Puntos + 1
print(f"Puntos: {Puntos}")