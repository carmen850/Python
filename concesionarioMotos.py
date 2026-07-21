

"""
Ejercicio POO — Concesionario de motos
--------------------------------------
Conceptos:
- Encapsulación (atributos privados)
- Herencia (tipos de motos)
- Polimorfismo (mostrar_info)
- Gestión de inventario
"""

# ------------------ Clase base ------------------

class Moto:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Encapsulación
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


# ------------------ Tipos de motos ------------------

class MotoGasolina(Moto):
    def __init__(self, marca, modelo, precio, cilindrada):
        super().__init__(marca, modelo, precio)
        self.__cilindrada = cilindrada

    def mostrar_info(self):
        print(f"Gasolina: {self.get_marca()} {self.get_modelo()} — {self.get_precio()}€ — {self.__cilindrada}cc")


class MotoDiesel(Moto):
    def __init__(self, marca, modelo, precio, consumo):
        super().__init__(marca, modelo, precio)
        self.__consumo = consumo  # litros/100km

    def mostrar_info(self):
        print(f"Diésel: {self.get_marca()} {self.get_modelo()} — {self.get_precio()}€ — {self.__consumo} L/100km")


class MotoElectrica(Moto):
    def __init__(self, marca, modelo, precio, autonomia):
        super().__init__(marca, modelo, precio)
        self.__autonomia = autonomia  # km

    def mostrar_info(self):
        print(f"Eléctrica: {self.get_marca()} {self.get_modelo()} — {self.get_precio()}€ — {self.__autonomia} km de autonomía")


class MotoHibrida(Moto):
    def __init__(self, marca, modelo, precio, modo):
        super().__init__(marca, modelo, precio)
        self.__modo = modo  # Eco, Sport, Mixto

    def mostrar_info(self):
        print(f"Híbrida: {self.get_marca()} {self.get_modelo()} — {self.get_precio()}€ — Modo {self.__modo}")


# ------------------ Concesionario ------------------

class ConcesionarioMotos:
    def __init__(self):
        self.inventario = []

    def agregar_moto(self, moto):
        self.inventario.append(moto)
        print("Moto añadida al inventario.")

    def listar_motos(self):
        if not self.inventario:
            print("No hay motos en el concesionario.")
            return
        for m in self.inventario:
            m.mostrar_info()

    def buscar_por_marca(self, marca):
        resultados = [m for m in self.inventario if m.get_marca().lower() == marca.lower()]
        if not resultados:
            print("No se encontraron motos de esa marca.")
            return
        for m in resultados:
            m.mostrar_info()


# ------------------ Ejecución ------------------

if __name__ == "__main__":
    concesionario = ConcesionarioMotos()

    m1 = MotoGasolina("Honda", "CBR600", 9500, 600)
    m2 = MotoDiesel("Royal Enfield", "Diesel Classic", 7200, 3.5)
    m3 = MotoElectrica("Zero", "SR/F", 19000, 260)
    m4 = MotoHibrida("Yamaha", "HybridX", 15000, "Eco")

    concesionario.agregar_moto(m1)
    concesionario.agregar_moto(m2)
    concesionario.agregar_moto(m3)
    concesionario.agregar_moto(m4)

    print("\n--- Inventario completo ---")
    concesionario.listar_motos()

    print("\n--- Buscar por marca 'Honda' ---")
    concesionario.buscar_por_marca("Honda")
