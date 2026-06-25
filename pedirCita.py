citas = []   # Lista donde guardaremos las citas

def pedir_cita():
    print("\n--- PEDIR CITA ---")
    nombre = input("Nombre del paciente: ")
    especialidad = input("Especialidad (Pediatría, Traumatología, Dermatología...): ")
    fecha = input("Fecha (dd/mm/aaaa): ")
    hora = input("Hora (hh:mm): ")

    cita = {
        "nombre": nombre,
        "especialidad": especialidad,
        "fecha": fecha,
        "hora": hora
    }

    citas.append(cita)
    print("✔ Cita registrada correctamente")

def ver_citas():
    print("\n--- LISTADO DE CITAS ---")
    if not citas:
        print("No hay citas registradas")
        return

    for i, cita in enumerate(citas, start=1):
        print(f"{i}. {cita['nombre']} - {cita['especialidad']} - {cita['fecha']} {cita['hora']}")

def cancelar_cita():
    print("\n--- CANCELAR CITA ---")
    ver_citas()

    if not citas:
        return

    num = int(input("Número de cita a cancelar: "))
    if 1 <= num <= len(citas):
        eliminada = citas.pop(num - 1)
        print(f"✔ Cita de {eliminada['nombre']} cancelada")
    else:
        print("Número no válido")

# ---------------- MENÚ PRINCIPAL ----------------

while True:
    print("\n===== HOSPITAL - GESTIÓN DE CITAS =====")
    print("1. Pedir cita")
    print("2. Ver citas")
    print("3. Cancelar cita")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        pedir_cita()
    elif opcion == "2":
        ver_citas()
    elif opcion == "3":
        cancelar_cita()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida")
