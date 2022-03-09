class Restaurant:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre  # Atributo
        self.categoria = categoria
        self.precio = precio  # Default: Public, _PROTECTED, __PRIVATE

    def mostrar_informacion(self):
        print(
            f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}"
        )

    # GETTERS Y SETTERS - Get = Obtiene un valor, SET = Agrega un alor
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio


# Crear una Clase hijo/herencia de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio)
        self.alberca = alberca

    def get_alberca(self):
        return self.alberca

    # Reescribir un metodo (debe llamarse igual)
    def mostrar_informacion(self):
        print(
            f"Nombre {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}"
        )


hotel = Hotel("Hotel POO", "5 Estrellas", 200, "Si")
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)
hotel.mostrar_informacion()
