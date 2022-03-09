class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")


# Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant("Burger King")
restaurant.mostrar_informacion()

print(restaurant)  # Solo Muestra la direccion de la clase

restaurant2 = Restaurant()
restaurant2.agregar_restaurant("La pizzada")
restaurant2.mostrar_informacion()

# Mostrar la informacion
print(f"Nombre Restaurant: {restaurant.nombre}")
print(f"Nombre Restaurant: {restaurant2.nombre}")
