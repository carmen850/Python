

"""
Ejercicio POO — Inmobiliaria
----------------------------
Conceptos:
- Encapsulación (atributos privados)
- Herencia (tipos de propiedades)
- Polimorfismo (mostrar_info)
- Gestión de inventario
"""

# ------------------ Clase base ------------------

class Propiedad:
    def __init__(self, direccion, precio):
        self.__direccion = direccion
        self.__precio = precio

    # Encapsulación
    def get_direccion(self):
        return self.__direccion

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    # Polimorfismo
    def mostrar_info(self):
        print(f"Propiedad en {self.__direccion} — {self.__precio}€")


# ------------------ Tipos de propiedades ------------------

class Casa(Propiedad):
    def __init__(self, direccion, precio, habitaciones, jardin):
        super().__init__(direccion, precio)
        self.__habitaciones = habitaciones
        self.__jardin = jardin  # True/False

    def mostrar_info(self):
        jardin_txt = "con jardín" if self.__jardin else "sin jardín"
        print(f"Casa: {self.get_direccion()} — {self.get_precio()}€ — {self.__habitaciones} hab — {jardin_txt}")


class Piso(Propiedad):
    def __init__(self, direccion, precio, planta, ascensor):
        super().__init__(direccion, precio)
        self.__planta = planta
        self.__ascensor = ascensor

    def mostrar_info(self):
        ascensor_txt = "con ascensor" if self.__ascensor else "sin ascensor"
        print(f"Piso: {self.get_direccion()} — {self.get_precio()}€ — Planta {self.__planta} — {ascensor_txt}")


class LocalComercial(Propiedad):
    def __init__(self, direccion, precio, metros):
        super().__init__(direccion, precio)
        self.__metros = metros

    def mostrar_info(self):
        print(f"Local comercial: {self.get_direccion()} — {self.get_precio()}€ — {self.__metros} m²")


# ------------------ Inmobiliaria ------------------

class Inmobiliaria:
    def __init__(self):
        self.inventario = []

    def agregar_propiedad(self, propiedad):
        self.inventario.append(propiedad)
        print("Propiedad añadida al inventario.")

    def listar_propiedades(self):
        if not self.inventario:
            print("No hay propiedades disponibles.")
            return
        for p in self.inventario:
            p.mostrar_info()

    def buscar_por_precio(self, max_precio):
        resultados = [p for p in self.inventario if p.get_precio() <= max_precio]
        if not resultados:
            print("No se encontraron propiedades dentro de ese precio.")
            return
        for p in resultados:
            p.mostrar_info()


# ------------------ Ejecución ------------------

if __name__ == "__main__":
    inmobiliaria = Inmobiliaria()

    casa1 = Casa("Calle Mayor 12", 250000, 4, True)
    piso1 = Piso("Avenida Sol 45", 180000, 3, True)
    local1 = LocalComercial("Calle Comercio 8", 95000, 120)

    inmobiliaria.agregar_propiedad(casa1)
    inmobiliaria.agregar_propiedad(piso1)
    inmobiliaria.agregar_propiedad(local1)

    print("\n--- Inventario completo ---")
    inmobiliaria.listar_propiedades()

    print("\n--- Buscar propiedades por precio máximo 200000€ ---")
    inmobiliaria.buscar_por_precio(200000)
