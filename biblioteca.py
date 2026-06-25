biblioteca = []   # Lista de libros

def agregar_libro():
    print("\n--- AGREGAR LIBRO ---")
    titulo = input("Título: ")
    autor = input("Autor: ")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "alquilado": False,
        "usuario": None
    }

    biblioteca.append(libro)
    print("✔ Libro añadido correctamente")

def ver_libros():
    print("\n--- LISTA DE LIBROS ---")
    if not biblioteca:
        print("No hay libros registrados")
        return

    for i, libro in enumerate(biblioteca, start=1):
        estado = "ALQUILADO" if libro["alquilado"] else "DISPONIBLE"
        print(f"{i}. {libro['titulo']} - {libro['autor']} [{estado}]")

def alquilar_libro():
    print("\n--- ALQUILAR LIBRO ---")
    ver_libros()

    if not biblioteca:
        return

    num = int(input("Número del libro a alquilar: "))

    if 1 <= num <= len(biblioteca):
        libro = biblioteca[num - 1]

        if libro["alquilado"]:
            print("❌ Ese libro ya está alquilado")
        else:
            usuario = input("Nombre del usuario que lo alquila: ")
            libro["alquilado"] = True
            libro["usuario"] = usuario
            print(f"✔ Libro '{libro['titulo']}' alquilado a {usuario}")
    else:
        print("Número no válido")

def devolver_libro():
    print("\n--- DEVOLVER LIBRO ---")
    ver_libros()

    if not biblioteca:
        return

    num = int(input("Número del libro a devolver: "))

    if 1 <= num <= len(biblioteca):
        libro = biblioteca[num - 1]

        if not libro["alquilado"]:
            print("❌ Ese libro no está alquilado")
        else:
            libro["alquilado"] = False
            libro["usuario"] = None
            print(f"✔ Libro '{libro['titulo']}' devuelto correctamente")
    else:
        print("Número no válido")

# ---------------- MENÚ PRINCIPAL ----------------

while True:
    print("\n===== BIBLIOTECA - SISTEMA DE ALQUILER =====")
    print("1. Agregar libro")
    print("2. Ver libros")
    print("3. Alquilar libro")
    print("4. Devolver libro")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        ver_libros()
    elif opcion == "3":
        alquilar_libro()
    elif opcion == "4":
        devolver_libro()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida")
