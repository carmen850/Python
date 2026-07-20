

"""
VetManager — Sistema de gestión veterinaria
-------------------------------------------
Funciones:
- Registrar animales (Perro, Gato)
- Eliminar pacientes
- Actualizar datos
- Listar pacientes
- Buscar por nombre
- Control de vacunas
- Persistencia en JSON

Uso:
    python vet_manager.py
"""

import json
import os

DATA_FILE = "pacientes.json"


# ------------------ Clases ------------------

class Animal:
    def __init__(self, id_animal, nombre, especie, edad, vacunado):
        self.id_animal = id_animal
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.vacunado = vacunado

    def to_dict(self):
        return {
            "id": self.id_animal,
            "nombre": self.nombre,
            "especie": self.especie,
            "edad": self.edad,
            "vacunado": self.vacunado
        }


class Perro(Animal):
    def __init__(self, id_animal, nombre, edad, vacunado):
        super().__init__(id_animal, nombre, "Perro", edad, vacunado)


class Gato(Animal):
    def __init__(self, id_animal, nombre, edad, vacunado):
        super().__init__(id_animal, nombre, "Gato", edad, vacunado)


# ------------------ Sistema ------------------

class Veterinaria:
    def __init__(self):
        self.pacientes = []
        self.load_data()

    # -------- Persistencia --------

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for p in data:
                    if p["especie"] == "Perro":
                        animal = Perro(p["id"], p["nombre"], p["edad"], p["vacunado"])
                    elif p["especie"] == "Gato":
                        animal = Gato(p["id"], p["nombre"], p["edad"], p["vacunado"])
                    else:
                        animal = Animal(p["id"], p["nombre"], p["especie"], p["edad"], p["vacunado"])
                    self.pacientes.append(animal)

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.pacientes], f, indent=4, ensure_ascii=False)

    # -------- CRUD --------

    def registrar_paciente(self, especie, nombre, edad):
        nuevo_id = 1 if not self.pacientes else self.pacientes[-1].id_animal + 1

        if especie.lower() == "perro":
            animal = Perro(nuevo_id, nombre, edad, vacunado=False)
        elif especie.lower() == "gato":
            animal = Gato(nuevo_id, nombre, edad, vacunado=False)
        else:
            animal = Animal(nuevo_id, nombre, especie.capitalize(), edad, vacunado=False)

        self.pacientes.append(animal)
        self.save_data()
        print(f"Paciente '{nombre}' registrado con ID {nuevo_id}")

    def eliminar_paciente(self, id_animal):
        for p in self.pacientes:
            if p.id_animal == id_animal:
                self.pacientes.remove(p)
                self.save_data()
                print("Paciente eliminado.")
                return
        print("ID no encontrado.")

    def actualizar_paciente(self, id_animal, nombre=None, edad=None):
        for p in self.pacientes:
            if p.id_animal == id_animal:
                if nombre:
                    p.nombre = nombre
                if edad:
                    p.edad = edad
                self.save_data()
                print("Datos actualizados.")
                return
        print("ID no encontrado.")

    def listar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        for p in self.pacientes:
            estado = "Vacunado" if p.vacunado else "Pendiente"
            print(f"[{p.id_animal}] {p.nombre} — {p.especie} — {p.edad} años — {estado}")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.pacientes if nombre.lower() in p.nombre.lower()]
        if not resultados:
            print("No se encontraron coincidencias.")
            return
        for p in resultados:
            estado = "Vacunado" if p.vacunado else "Pendiente"
            print(f"[{p.id_animal}] {p.nombre} — {p.especie} — {p.edad} años — {estado}")

    def vacunar(self, id_animal):
        for p in self.pacientes:
            if p.id_animal == id_animal:
                p.vacunado = True
                self.save_data()
                print("Vacuna registrada.")
                return
        print("ID no encontrado.")

    # -------- Menú --------

    def menu(self):
        while True:
            print("\n=== VET MANAGER ===")
            print("1. Registrar paciente")
            print("2. Eliminar paciente")
            print("3. Actualizar paciente")
            print("4. Listar pacientes")
            print("5. Buscar por nombre")
            print("6. Registrar vacuna")
            print("7. Salir")

            opcion = input("Seleccione opción: ")

            if opcion == "1":
                especie = input("Especie (Perro/Gato/Otro): ")
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                self.registrar_paciente(especie, nombre, edad)

            elif opcion == "2":
                id_animal = int(input("ID del paciente: "))
                self.eliminar_paciente(id_animal)

            elif opcion == "3":
                id_animal = int(input("ID del paciente: "))
                nombre = input("Nuevo nombre (enter para no cambiar): ")
                edad = input("Nueva edad (enter para no cambiar): ")
                self.actualizar_paciente(id_animal, nombre or None, int(edad) if edad else None)

            elif opcion == "4":
                self.listar_pacientes()

            elif opcion == "5":
                nombre = input("Nombre a buscar: ")
                self.buscar_por_nombre(nombre)

            elif opcion == "6":
                id_animal = int(input("ID del paciente: "))
                self.vacunar(id_animal)

            elif opcion == "7":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
                

if __name__ == "__main__":
    Veterinaria().menu()
