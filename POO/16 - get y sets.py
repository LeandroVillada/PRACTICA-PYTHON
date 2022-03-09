class Restaurant:
    def __init__(self, nombre, categoria, __precio):
        self.nombre = nombre  # Atributo
        self.categoria = categoria
        self.__precio = __precio  # Default: Public, _PROTECTED, __PRIVATE

    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}"
        )

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un alor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


# Instanciar la clase
restaurant = Restaurant("Burger King", "Hamburguesa", 50)
precio = restaurant.get_precio()
print(precio)
restaurant.set_precio(80)
restaurant.mostrar_informacion()

# print(restaurant)  # Solo Muestra la direccion de la clase

restaurant2 = Restaurant("La pizzada", "Pizzas", 25)
precio = restaurant.get_precio()
print(precio)
restaurant2.set_precio(80)
restaurant2.mostrar_informacion()

# Mostrar la informacion
# print(f"Nombre Restaurant: {restaurant.nombre}")
# print(f"Nombre Restaurant: {restaurant2.nombre}")
