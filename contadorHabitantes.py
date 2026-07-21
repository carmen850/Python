

"""
Ejercicio POO — Contador de habitantes de un pueblo
---------------------------------------------------
Conceptos:
- Encapsulación
- Gestión de habitantes
- Contador automático
"""

# ------------------ Clase Habitante ------------------

class Habitante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # Encapsulación: getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def mostrar_info(self):
        print(f"{self.__nombre} — {self.__edad} años")


# ------------------ Clase Pueblo ------------------

class Pueblo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__habitantes = []

    def agregar_habitante(self, habitante):
        self.__habitantes.append(habitante)
        print(f"Habitante '{habitante.get_nombre()}' añadido.")

    def eliminar_habitante(self, nombre):
        for h in self.__habitantes:
            if h.get_nombre().lower() == nombre.lower():
                self.__habitantes.remove(h)
                print(f"Habitante '{nombre}' eliminado.")
                return
        print("Habitante no encontrado.")

    def contar_habitantes(self):
        return len(self.__habitantes)

    def listar_habitantes(self):
        if not self.__habitantes:
            print("No hay habitantes registrados.")
            return
        for h in self.__habitantes:
            h.mostrar_info()


# ------------------ Ejecución ------------------

if __name__ == "__main__":
    pueblo = Pueblo("San Sebastián de los Reyes")

    h1 = Habitante("Carmen", 35)
    h2 = Habitante("Luis", 42)
    h3 = Habitante("Ana", 12)

    pueblo.agregar_habitante(h1)
    pueblo.agregar_habitante(h2)
    pueblo.agregar_habitante(h3)

    print("\n--- Habitantes del pueblo ---")
    pueblo.listar_habitantes()

    print("\n--- Total de habitantes ---")
    print(pueblo.contar_habitantes())

    print("\n--- Eliminando a Ana ---")
    pueblo.eliminar_habitante("Ana")

    print("\n--- Total actualizado ---")
    print(pueblo.contar_habitantes())
