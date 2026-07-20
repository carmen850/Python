

"""
HealthCenter — Sistema de gestión de pacientes y citas médicas
--------------------------------------------------------------
Funciones:
- Registrar pacientes
- Eliminar pacientes
- Actualizar datos
- Listar pacientes
- Buscar por nombre
- Registrar citas médicas
- Listar citas
- Persistencia en JSON

Uso:
    python health_center.py
"""

import json
import os

PACIENTES_FILE = "pacientes.json"
CITAS_FILE = "citas.json"


# ------------------ Clases ------------------

class Paciente:
    def __init__(self, id_paciente, nombre, edad, alergias):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.alergias = alergias

    def to_dict(self):
        return {
            "id": self.id_paciente,
            "nombre": self.nombre,
            "edad": self.edad,
            "alergias": self.alergias
        }


class Cita:
    def __init__(self, id_cita, id_paciente, fecha, motivo):
        self.id_cita = id_cita
        self.id_paciente = id_paciente
        self.fecha = fecha
        self.motivo = motivo

    def to_dict(self):
        return {
            "id": self.id_cita,
            "id_paciente": self.id_paciente,
            "fecha": self.fecha,
            "motivo": self.motivo
        }


# ------------------ Sistema ------------------

class CentroSalud:
    def __init__(self):
        self.pacientes = []
        self.citas = []
        self.load_data()

    # -------- Persistencia --------

    def load_data(self):
        if os.path.exists(PACIENTES_FILE):
            with open(PACIENTES_FILE, "r", encoding="utf-8") as f:
                for p in json.load(f):
                    paciente = Paciente(p["id"], p["nombre"], p["edad"], p["alergias"])
                    self.pacientes.append(paciente)

        if os.path.exists(CITAS_FILE):
            with open(CITAS_FILE, "r", encoding="utf-8") as f:
                for c in json.load(f):
                    cita = Cita(c["id"], c["id_paciente"], c["fecha"], c["motivo"])
                    self.citas.append(cita)

    def save_data(self):
        with open(PACIENTES_FILE, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.pacientes], f, indent=4, ensure_ascii=False)

        with open(CITAS_FILE, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.citas], f, indent=4, ensure_ascii=False)

    # -------- CRUD Pacientes --------

    def registrar_paciente(self, nombre, edad, alergias):
        nuevo_id = 1 if not self.pacientes else self.pacientes[-1].id_paciente + 1
        paciente = Paciente(nuevo_id, nombre, edad, alergias)
        self.pacientes.append(paciente)
        self.save_data()
        print(f"Paciente '{nombre}' registrado con ID {nuevo_id}")

    def eliminar_paciente(self, id_paciente):
        for p in self.pacientes:
            if p.id_paciente == id_paciente:
                self.pacientes.remove(p)
                self.save_data()
                print("Paciente eliminado.")
                return
        print("ID no encontrado.")

    def actualizar_paciente(self, id_paciente, nombre=None, edad=None, alergias=None):
        for p in self.pacientes:
            if p.id_paciente == id_paciente:
                if nombre:
                    p.nombre = nombre
                if edad:
                    p.edad = edad
                if alergias:
                    p.alergias = alergias
                self.save_data()
                print("Datos actualizados.")
                return
        print("ID no encontrado.")

    def listar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        for p in self.pacientes:
            print(f"[{p.id_paciente}] {p.nombre} — {p.edad} años — Alergias: {p.alergias}")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.pacientes if nombre.lower() in p.nombre.lower()]
        if not resultados:
            print("No se encontraron coincidencias.")
            return
        for p in resultados:
            print(f"[{p.id_paciente}] {p.nombre} — {p.edad} años — Alergias: {p.alergias}")

    # -------- Citas Médicas --------

    def registrar_cita(self, id_paciente, fecha, motivo):
        if not any(p.id_paciente == id_paciente for p in self.pacientes):
            print("El paciente no existe.")
            return

        nuevo_id = 1 if not self.citas else self.citas[-1].id_cita + 1
        cita = Cita(nuevo_id, id_paciente, fecha, motivo)
        self.citas.append(cita)
        self.save_data()
        print(f"Cita registrada con ID {nuevo_id}")

    def listar_citas(self):
        if not self.citas:
            print("No hay citas registradas.")
            return
        for c in self.citas:
            print(f"[{c.id_cita}] Paciente {c.id_paciente} — {c.fecha} — Motivo: {c.motivo}")

    # -------- Menú --------

    def menu(self):
        while True:
            print("\n=== HEALTH CENTER ===")
            print("1. Registrar paciente")
            print("2. Eliminar paciente")
            print("3. Actualizar paciente")
            print("4. Listar pacientes")
            print("5. Buscar paciente por nombre")
            print("6. Registrar cita médica")
            print("7. Listar citas")
            print("8. Salir")

            opcion = input("Seleccione opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                alergias = input("Alergias: ")
                self.registrar_paciente(nombre, edad, alergias)

            elif opcion == "2":
                id_paciente = int(input("ID del paciente: "))
                self.eliminar_paciente(id_paciente)

            elif opcion == "3":
                id_paciente = int(input("ID del paciente: "))
                nombre = input("Nuevo nombre (enter para no cambiar): ")
                edad = input("Nueva edad (enter para no cambiar): ")
                alergias = input("Nuevas alergias (enter para no cambiar): ")
                self.actualizar_paciente(
                    id_paciente,
                    nombre or None,
                    int(edad) if edad else None,
                    alergias or None
                )

            elif opcion == "4":
                self.listar_pacientes()

            elif opcion == "5":
                nombre = input("Nombre a buscar: ")
                self.buscar_por_nombre(nombre)

            elif opcion == "6":
                id_paciente = int(input("ID del paciente: "))
                fecha = input("Fecha (dd/mm/aaaa): ")
                motivo = input("Motivo: ")
                self.registrar_cita(id_paciente, fecha, motivo)

            elif opcion == "7":
                self.listar_citas()

            elif opcion == "8":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
                

if __name__ == "__main__":
    CentroSalud().menu()
