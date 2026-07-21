

"""
Ejercicio POO — Concesionario de coches
---------------------------------------
Conceptos:
- Encapsulación (atributos privados)
- Herencia (Coche y SUV heredan de Vehiculo)
- Polimorfismo (método mostrar_info)
- Gestión de inventario
"""

# ------------------ Clase base ------------------

class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Encapsulación: getters y setters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    # Polimorfismo
    def mostrar_info(self):
        print(f"{self.__marca} {self.__modelo} — {self.__precio}€")


# ------------------ Clase hija: Coche ------------------

class Coche(Vehiculo):
    def __init__(self, marca, modelo, precio, puertas):
        super().__init__(marca, modelo, precio)
        self.__puertas = puertas

    def mostrar_info(self):
        print(f"Coche: {self.get_marca()} {self.get_modelo()} — {self.get_precio()}€ — {self.__puertas} puertas")


# ------------------ Clase hija: SUV ------------------

class SUV(Vehiculo):
    def __init__(self, marca, modelo, precio, traccion):
        super().__init__(marca, modelo, precio)
        self.__traccion = traccion  # 4x4, delantera, etc.

    def mostrar_info(self):
        print(f"SUV: {self.get_marca()} {self.get_modelo()} — {self.get_precio()}€ — Tracción {self.__traccion}")


# ------------------ Clase Concesionario ------------------

class Concesionario:
    def __init__(self):
        self.inventario = []

    def agregar_vehiculo(self, vehiculo):
        self.inventario.append(vehiculo)
        print("Vehículo añadido al inventario.")

    def listar_vehiculos(self):
        if not self.inventario:
            print("No hay vehículos en el concesionario.")
            return
        for v in self.inventario:
            v.mostrar_info()

    def buscar_por_marca(self, marca):
        resultados = [v for v in self.inventario if v.get_marca().lower() == marca.lower()]
        if not resultados:
            print("No se encontraron vehículos de esa marca.")
            return
        for v in resultados:
            v.mostrar_info()


# ------------------ Ejecución ------------------

if __name__ == "__main__":
    concesionario = Concesionario()

    coche1 = Coche("Toyota", "Corolla", 18000, 5)
    suv1 = SUV("Nissan", "Qashqai", 25000, "4x4")
    coche2 = Coche("Ford", "Focus", 17000, 3)

    concesionario.agregar_vehiculo(coche1)
    concesionario.agregar_vehiculo(suv1)
    concesionario.agregar_vehiculo(coche2)

    print("\n--- Inventario completo ---")
    concesionario.listar_vehiculos()

    print("\n--- Buscar por marca 'Toyota' ---")
    concesionario.buscar_por_marca("Toyota")
