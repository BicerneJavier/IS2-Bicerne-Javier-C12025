from ..Negocio.bibliotecaService import BibliotecaService, BibliotecaError

def cargar_datos_iniciales(servicio: BibliotecaService):
    try:
        # --- AUTORES ---
        autor1 = servicio.registrar_autor("Gabriel", "García Márquez")
        autor2 = servicio.registrar_autor("JK", "Rowling")
        autor3 = servicio.registrar_autor("George", "Orwell")

        # --- CATEGORÍAS ---
        cat1 = servicio.registrar_categoria("Ficción")
        cat2 = servicio.registrar_categoria("Ciencia Ficción")
        cat3 = servicio.registrar_categoria("Novela")

        # --- SOCIOS ---
        servicio.registrar_socio("Juan", "Pérez", "12345678")
        servicio.registrar_socio("María", "Gómez", "87654321")

        # --- LIBROS ---
        servicio.registrar_libro("Cien años de soledad", autor1.autorID, cat3.categoriaID, "1967-05-30")
        servicio.registrar_libro("Harry Potter y la piedra filosofal", autor2.autorID, cat1.categoriaID, "1997-06-26")
        servicio.registrar_libro("1984", autor3.autorID, cat2.categoriaID, "1949-06-08")

        print("Datos iniciales cargados correctamente.")
    except BibliotecaError as e:
        print(f"Error al cargar datos iniciales: {e}")