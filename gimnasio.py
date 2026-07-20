

"""
GymManager — Sistema de gestión de socios del gimnasio
------------------------------------------------------
Funciones:
- Registrar socios
- Eliminar socios
- Actualizar datos
- Listar socios
- Buscar por nombre
- Control de pagos (cuota al día / pendiente)
- Persistencia en JSON

Uso:
    python gym_manager.py
"""

import json
import os


DATA_FILE = "socios.json"


class Socio:
    def __init__(self, id_socio, nombre, edad, cuota_pagada):
        self.id_socio = id_socio
        self.nombre = nombre
        self.edad = edad
        self.cuota_pagada = cuota_pagada  # True / False

    def to_dict(self):
        return {
            "id": self.id_socio,
            "nombre": self.nombre,
            "edad": self.edad,
            "cuota_pagada": self.cuota_pagada
        }


class Gimnasio:
    def __init__(self):
        self.socios = []
        self.load_data()

    # ------------------ Persistencia ------------------

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for s in data:
                    socio = Socio(
                        s["id"], s["nombre"], s["edad"], s["cuota_pagada"]
                    )
                    self.socios.append(socio)

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.socios], f, indent=4, ensure_ascii=False)

    # ------------------ CRUD ------------------

    def agregar_socio(self, nombre, edad):
        nuevo_id = 1 if not self.socios else self.socios[-1].id_socio + 1
        socio = Socio(nuevo_id, nombre, edad, cuota_pagada=False)
        self.socios.append(socio)
        self.save_data()
        print(f"Socio '{nombre}' registrado con ID {nuevo_id}")

    def eliminar_socio(self, id_socio):
        for s in self.socios:
            if s.id_socio == id_socio:
                self.socios.remove(s)
                self.save_data()
                print(f"Socio con ID {id_socio} eliminado")
                return
        print("ID no encontrado")

    def actualizar_socio(self, id_socio, nombre=None, edad=None):
        for s in self.socios:
            if s.id_socio == id_socio:
                if nombre:
                    s.nombre = nombre
                if edad:
                    s.edad = edad
                self.save_data()
                print("Datos actualizados")
                return
        print("ID no encontrado")

    def listar_socios(self):
        if not self.socios:
            print("No hay socios registrados.")
            return
        for s in self.socios:
            estado = "Al día" if s.cuota_pagada else "Pendiente"
            print(f"[{s.id_socio}] {s.nombre} — {s.edad} años — Cuota: {estado}")

    def buscar_por_nombre(self, nombre):
        resultados = [s for s in self.socios if nombre.lower() in s.nombre.lower()]
        if not resultados:
            print("No se encontraron coincidencias.")
            return
        for s in resultados:
            estado = "Al día" if s.cuota_pagada else "Pendiente"
            print(f"[{s.id_socio}] {s.nombre} — {s.edad} años — Cuota: {estado}")

    def pagar_cuota(self, id_socio):
        for s in self.socios:
            if s.id_socio == id_socio:
                s.cuota_pagada = True
                self.save_data()
                print("Cuota marcada como pagada.")
                return
        print("ID no encontrado")

    # ------------------ Menú ------------------

    def menu(self):
        while True:
            print("\n=== GYM MANAGER ===")
            print("1. Registrar socio")
            print("2. Eliminar socio")
            print("3. Actualizar socio")
            print("4. Listar socios")
            print("5. Buscar por nombre")
            print("6. Marcar cuota como pagada")
            print("7. Salir")

            opcion = input("Seleccione opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                self.agregar_socio(nombre, edad)

            elif opcion == "2":
                id_socio = int(input("ID del socio: "))
                self.eliminar_socio(id_socio)

            elif opcion == "3":
                id_socio = int(input("ID del socio: "))
                nombre = input("Nuevo nombre (enter para no cambiar): ")
                edad = input("Nueva edad (enter para no cambiar): ")
                self.actualizar_socio(id_socio, nombre or None, int(edad) if edad else None)

            elif opcion == "4":
                self.listar_socios()

            elif opcion == "5":
                nombre = input("Nombre a buscar: ")
                self.buscar_por_nombre(nombre)

            elif opcion == "6":
                id_socio = int(input("ID del socio: "))
                self.pagar_cuota(id_socio)

            elif opcion == "7":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
                

if __name__ == "__main__":
    Gimnasio().menu()
