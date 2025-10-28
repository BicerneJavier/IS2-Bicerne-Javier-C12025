from ..Negocio.bibliotecaService import BibliotecaService, BibliotecaError
from .datos_iniciales import cargar_datos_iniciales

def mostrar_lista(elementos, mensaje_vacio):
    if elementos:
        for e in elementos:
            print(e)
    else:
        print(f"⚠️   {mensaje_vacio}")

def solicitar_id_numerico(mensaje):
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("❌ ID inválido. Debe ser un número.")

# ---------------------- SUBMENÚ AUTORES ----------------------
def submenu_autores(servicio: BibliotecaService):
    while True:
        print("\n📚  ===  SUBMENÚ AUTORES  ===")
        print("1️⃣   Registrar autor")
        print("2️⃣   Listar autores")
        print("3️⃣   Eliminar autor")
        print("0️⃣   Volver")
        opcion = input("👉  Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("🖊️   Nombre del autor: ")
                apellido = input("🖊️   Apellido del autor: ")
                autor = servicio.registrar_autor(nombre, apellido)
                print(f"✅ Autor '{autor.nombre} {autor.apellido}' registrado con ID: {autor.autorID}")

            elif opcion == "2":
                mostrar_lista(servicio.listar_autores(), "No hay autores registrados.")

            elif opcion == "3":
                autorID = solicitar_id_numerico("🗑️   ID del autor a eliminar: ")
                autor_eliminado = servicio.eliminar_autor(autorID)
                print(f"🗑️   Autor '{autor_eliminado.nombre} {autor_eliminado.apellido}' eliminado correctamente.")

            elif opcion == "0":
                print("↩️   Volviendo al menú principal...")
                break
            else:
                print("⚠️   Opción no válida.")
        except (BibliotecaError, ValueError) as e:
            print(f"❌   Error: {e}")

# ---------------------- SUBMENÚ CATEGORÍAS ----------------------
def submenu_categorias(servicio: BibliotecaService):
    while True:
        print("\n🏷️   ===  SUBMENÚ CATEGORÍAS  ===")
        print(" 1️⃣   Registrar categoría")
        print(" 2️⃣   Listar categorías")
        print(" 3️⃣   Eliminar categoría")
        print(" 0️⃣   Volver")
        opcion = input("👉  Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("🖊️ Nombre de la categoría: ")
                categoria = servicio.registrar_categoria(nombre)
                print(f"✅   Categoría '{categoria.nombre}' registrada con ID: {categoria.categoriaID}")

            elif opcion == "2":
                mostrar_lista(servicio.listar_categorias(), "No hay categorías registradas.")

            elif opcion == "3":
                categoriaID = solicitar_id_numerico("🗑️   ID de la categoría a eliminar: ")
                cat_eliminada = servicio.eliminar_categoria(categoriaID)
                print(f"🗑️   Categoría '{cat_eliminada.nombre}' eliminada correctamente.")

            elif opcion == "0":
                print("↩️   Volviendo al menú principal...")
                break
            else:
                print("⚠️   Opción no válida.")
        except (BibliotecaError, ValueError) as e:
            print(f"❌   Error: {e}")

# ---------------------- SUBMENÚ LIBROS ----------------------
def submenu_libros(servicio: BibliotecaService):
    while True:
        print("\n📖  ===  SUBMENÚ LIBROS  ===")
        print("1️⃣   Registrar libro")
        print("2️⃣   Listar todos los libros")
        print("3️⃣   Listar libros disponibles")
        print("4️⃣   Eliminar libro")
        print("0️⃣   Volver")
        opcion = input("👉  Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                titulo = input("🖊️   Título del libro: ")
                autorID = solicitar_id_numerico("ID del autor: ")
                categoriaID = solicitar_id_numerico("ID de la categoría: ")
                fecha = input("📅   Fecha de publicación (YYYY-MM-DD): ")
                libro = servicio.registrar_libro(titulo, autorID, categoriaID, fecha)
                print(f"✅   Libro '{libro.titulo}' registrado con ID: {libro.libroID}")

            elif opcion == "2":
                mostrar_lista(servicio.listar_libros(), "No hay libros registrados.")

            elif opcion == "3":
                mostrar_lista(servicio.listar_libros_disponibles(), "No hay libros disponibles.")

            elif opcion == "4":
                libroID = solicitar_id_numerico("🗑️   ID del libro a eliminar: ")
                libro_eliminado = servicio.eliminar_libro(libroID)
                print(f"🗑️   Libro '{libro_eliminado.titulo}' eliminado correctamente.")

            elif opcion == "0":
                print("↩️   Volviendo al menú principal...")
                break
            else:
                print("⚠️   Opción no válida.")
        except (BibliotecaError, ValueError) as e:
            print(f"❌ Error: {e}")

# ---------------------- SUBMENÚ SOCIOS ----------------------
def submenu_socios(servicio: BibliotecaService):
    while True:
        print("\n👥  ===  SUBMENÚ SOCIOS  ===")
        print("1️⃣   Registrar socio")
        print("2️⃣   Listar socios")
        print("3️⃣   Listar socios activos")
        print("4️⃣   Desactivar socio")
        print("5️⃣   Activar socio")
        print("0️⃣   Volver")
        opcion = input("👉  Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                nombre = input("🖊️   Nombre del socio: ")
                apellido = input("🖊️  Apellido del socio: ")
                dni = input("🪪 DNI del socio: ")
                socio = servicio.registrar_socio(nombre, apellido, dni)
                print(f"✅ Socio '{socio.nombre} {socio.apellido}' registrado con ID: {socio.socioID}")

            elif opcion == "2":
                mostrar_lista(servicio.listar_socios(), "No hay socios registrados.")

            elif opcion == "3":
                mostrar_lista(servicio.listar_socios_activos(), "No hay socios activos.")

            elif opcion == "4":
                socioID = solicitar_id_numerico("🚫 ID del socio a desactivar: ")
                socio_desactivado = servicio.desactivar_socio(socioID)
                print(f"⚙️   Socio '{socio_desactivado.nombre} {socio_desactivado.apellido}' desactivado correctamente.")

            elif opcion == "5":
                socioID = solicitar_id_numerico("✅ ID del socio a activar: ")
                socio_activado = servicio.activar_socio(socioID)
                print(f"🔄   Socio '{socio_activado.nombre} {socio_activado.apellido}' reactivado correctamente.")

            elif opcion == "0":
                print("↩️   Volviendo al menú principal...")
                break
            else:
                print("⚠️   Opción no válida.")
        except (BibliotecaError, ValueError) as e:
            print(f"❌ Error: {e}")

# ---------------------- SUBMENÚ PRÉSTAMOS ----------------------
def submenu_prestamos(servicio: BibliotecaService):
    def mostrar_info_completa_prestamo(p_id):
        info = servicio.obtener_info_prestamo(p_id)
        if not info:
            print(f"⚠️   No se encontró ningún préstamo con ID {p_id}.")
            return

        p = info['prestamo']
        libro = info['libro']
        socio = info['socio']
        autor = servicio.buscar_autor(libro.autorID) if libro else None
        estado = "📗   Devuelto" if p.devuelto else "📘 Activo"

        print(f"\n🔎 --- Detalle del Préstamo ID: {p.prestamoID} ---")
        print(f"📌   Estado: {estado}")
        print(f"📖   Libro: {libro.titulo if libro else 'N/A'}")
        print(f"✍️   Autor: {autor if autor else 'N/A'}")
        print(f"👤   Socio: {socio if socio else 'N/A'}")
        print(f"📅   Fecha de préstamo: {p.fecha_prestamo}")
        if p.devuelto:
            print(f"📆   Fecha de devolución: {p.fecha_devolucion}")
        print("-------------------------------------")

    while True:
        print("\n📕  ===  SUBMENÚ PRÉSTAMOS  ===")
        print("1️⃣   Prestar libro")
        print("2️⃣   Devolver libro")
        print("3️⃣   Listar todos los préstamos")
        print("4️⃣   Listar préstamos activos")
        print("5️⃣   Listar préstamos por socio")
        print("6️⃣   Ver detalle de un préstamo")
        print("0️⃣   Volver")
        opcion = input("👉  Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                socioID = solicitar_id_numerico("👤   ID del socio: ")
                libroID = solicitar_id_numerico("📖   ID del libro: ")
                prestamo = servicio.prestar_libro(socioID, libroID)
                print(f"✅   Préstamo registrado con ID: {prestamo.prestamoID}")

            elif opcion == "2":
                prestamoID = solicitar_id_numerico("🔁 ID del préstamo a devolver: ")
                prestamo = servicio.devolver_libro(prestamoID)
                print(f"📗   Libro devuelto correctamente (ID Préstamo: {prestamo.prestamoID})")

            elif opcion == "3":
                mostrar_lista(servicio.listar_prestamos(), "No hay préstamos registrados.")

            elif opcion == "4":
                mostrar_lista(servicio.listar_prestamos_activos(), "No hay préstamos activos.")
                
            elif opcion == "5":
                socioID = solicitar_id_numerico("👤   ID del socio: ")
                mostrar_lista(servicio.listar_prestamos_por_socio(socioID), "No se encontraron préstamos para este socio.")

            elif opcion == "6":
                prestamoID = solicitar_id_numerico("🔍  ID del préstamo: ")
                mostrar_info_completa_prestamo(prestamoID)

            elif opcion == "0":
                print("↩️ Volviendo al menú principal...")
                break
            else:
                print("⚠️   Opción no válida.")
        except (BibliotecaError, ValueError) as e:
            print(f"❌   Error: {e}")

# ---------------------- MENÚ PRINCIPAL ----------------------
def menu_principal():
    servicio = BibliotecaService()
    cargar_datos_iniciales(servicio)

    while True:
        print("\n🏛️  ===  MENÚ PRINCIPAL BIBLIOTECA  ===")
        print("1️⃣   Autores")
        print("2️⃣   Categorías")
        print("3️⃣   Libros")
        print("4️⃣   Socios")
        print("5️⃣   Préstamos")
        print("0️⃣   Salir")

        opcion = input("👉  Seleccione una opción: ").strip()

        if opcion == "1":
            submenu_autores(servicio)
        elif opcion == "2":
            submenu_categorias(servicio)
        elif opcion == "3":
            submenu_libros(servicio)
        elif opcion == "4":
            submenu_socios(servicio)
        elif opcion == "5":
            submenu_prestamos(servicio)
        elif opcion == "0":
            print("👋   ¡Gracias por usar la biblioteca! Hasta pronto 📚")
            break
        else:
            print("⚠️   Opción no válida.")

if __name__ == "__main__":
    menu_principal()

