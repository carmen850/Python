

"""
Ejercicio POO — Gestión de obras
--------------------------------
Conceptos:
- Encapsulación
- Gestión de obras
- Informes semanales
"""

# ------------------ Clase Informe Semanal ------------------

class InformeSemanal:
    def __init__(self, semana, descripcion, avance):
        self.__semana = semana
        self.__descripcion = descripcion
        self.__avance = avance  # porcentaje

    def mostrar_informe(self):
        print(f"Semana {self.__semana}: {self.__descripcion} — Avance: {self.__avance}%")


# ------------------ Clase Obra ------------------

class Obra:
    def __init__(self, direccion, tecnico, empresa, tipo_reforma):
        self.__direccion = direccion
        self.__tecnico = tecnico
        self.__empresa = empresa
        self.__tipo_reforma = tipo_reforma
        self.__informes = []  # lista de informes semanales

    # Encapsulación: getters
    def get_direccion(self):
        return self.__direccion

    def get_tecnico(self):
        return self.__tecnico

    def get_empresa(self):
        return self.__empresa

    def get_tipo_reforma(self):
        return self.__tipo_reforma

    # Añadir informe semanal
    def agregar_informe(self, informe):
        self.__informes.append(informe)
        print("Informe semanal añadido.")

    # Mostrar todos los informes
    def mostrar_informes(self):
        if not self.__informes:
            print("No hay informes registrados.")
            return
        for inf in self.__informes:
            inf.mostrar_informe()

    # Mostrar información general de la obra
    def mostrar_info(self):
        print(f"Obra en {self.__direccion}")
        print(f"Técnico responsable: {self.__tecnico}")
        print(f"Empresa: {self.__empresa}")
        print(f"Tipo de reforma: {self.__tipo_reforma}")


# ------------------ Clase Gestor de Obras ------------------

class GestorObras:
    def __init__(self):
        self.__obras = []

    def agregar_obra(self, obra):
        self.__obras.append(obra)
        print("Obra registrada.")

    def listar_obras(self):
        if not self.__obras:
            print("No hay obras registradas.")
            return
        for o in self.__obras:
            print("\n--- Obra ---")
            o.mostrar_info()

    def buscar_por_direccion(self, direccion):
        resultados = [o for o in self.__obras if o.get_direccion().lower() == direccion.lower()]
        if not resultados:
            print("No se encontraron obras en esa dirección.")
            return
        for o in resultados:
            o.mostrar_info()
            print("\nInformes:")
            o.mostrar_informes()


# ------------------ Ejecución ------------------

if __name__ == "__main__":
    gestor = GestorObras()

    # Crear obras
    obra1 = Obra(
        "Calle Mayor 15",
        "Carmen López",
        "Reformas Madrid S.L.",
        "Reforma integral"
    )

    obra2 = Obra(
        "Avenida Sol 22",
        "Luis Martín",
        "Construcciones Vega",
        "Reforma de baño"
    )

    gestor.agregar_obra(obra1)
    gestor.agregar_obra(obra2)

    # Añadir informes semanales
    informe1 = InformeSemanal(1, "Demolición y retirada de escombros", 10)
    informe2 = InformeSemanal(2, "Instalación de fontanería", 35)

    obra1.agregar_informe(informe1)
    obra1.agregar_informe(informe2)

    print("\n--- Listado de obras ---")
    gestor.listar_obras()

    print("\n--- Buscar obra por dirección ---")
    gestor.buscar_por_direccion("Calle Mayor 15")
