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


# Crear una Clase hijo/herencia de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, __precio):
        super().__init__(nombre, categoria, __precio)

hotel = Hotel('Hotel POO', '5 Estrellas',200)
hotel.mostrar_informacion()