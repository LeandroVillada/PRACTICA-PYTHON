class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre    #Atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")


# Instanciar la clase
restaurant = Restaurant("Burger King",'Hamburguesa',50)
restaurant.mostrar_informacion()

print(restaurant)  # Solo Muestra la direccion de la clase

restaurant2 = Restaurant("La pizzada",'Pizzas',25)
restaurant2.mostrar_informacion()

# Mostrar la informacion
# print(f"Nombre Restaurant: {restaurant.nombre}")
# print(f"Nombre Restaurant: {restaurant2.nombre}")
