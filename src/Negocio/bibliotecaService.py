from ..Datos.Gestores.gestor_autores import GestorAutores
from ..Datos.Gestores.gestor_categoria import GestorCategorias
from ..Datos.Gestores.gestor_libros import GestorLibros
from ..Datos.Gestores.gestor_socio import GestorSocios
from ..Datos.Gestores.gestor_prestamos import GestorPrestamos
from ..Datos.Entidades.autor import Autor
from ..Datos.Entidades.categoria import Categoria
from ..Datos.Entidades.libro import Libro
from ..Datos.Entidades.socio import Socio
from ..Datos.Entidades.prestamo import Prestamo
from datetime import datetime

class BibliotecaError(Exception):
    #Excepción personalizada para errores de la biblioteca
    pass

class BibliotecaService:
    def __init__(self):
        self.__gestor_autores = GestorAutores()
        self.__gestor_categorias = GestorCategorias()
        self.__gestor_libros = GestorLibros()
        self.__gestor_socios = GestorSocios()
        self.__gestor_prestamos = GestorPrestamos()

    # ============================================================
    #                 MÉTODOS PRIVADOS DE APOYO
    # ============================================================

    def __generar_siguiente_id(self, elementos, id_attr_name):
        if not elementos:
            return 1
        return max([getattr(e, id_attr_name) for e in elementos]) + 1

    def __validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise BibliotecaError("El nombre no puede estar vacío.")
        if not all(c.isalpha() or c.isspace() for c in nombre):
            raise BibliotecaError("El nombre solo puede contener letras y espacios.")

    def __validar_dni(self, dni):
        if not dni or not dni.strip():
            raise BibliotecaError("El DNI no puede estar vacío.")
        if not dni.isdigit():
            raise BibliotecaError("El DNI solo puede contener números.")
        if len(dni) < 7 or len(dni) > 8:
            raise BibliotecaError("El DNI debe tener entre 7 y 8 dígitos.")

    def __validar_fecha(self, fecha_str):
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d')
        except ValueError:
            raise BibliotecaError("Formato de fecha inválido. Use YYYY-MM-DD.")

    # ============================================================
    #                         AUTORES
    # ============================================================

    def registrar_autor(self, nombre, apellido):
        self.__validar_nombre(nombre)
        self.__validar_nombre(apellido)
        
        autores = self.__gestor_autores.listar()
        autorID = self.__generar_siguiente_id(autores, 'autorID')
        autor = Autor(autorID, nombre.strip(), apellido.strip())
        self.__gestor_autores.agregar(autor)
        return autor

    def eliminar_autor(self, autorID):
        autor = self.__gestor_autores.buscar(autorID)
        if not autor:
            raise BibliotecaError(f"No se encontró ningún autor con ID {autorID}.")

        if self.__gestor_libros.buscar_por_autor(autorID):
            raise BibliotecaError("No se puede eliminar el autor porque tiene libros asociados.")

        self.__gestor_autores.eliminar(autorID)
        return autor

    def listar_autores(self):
        return self.__gestor_autores.listar()

    def buscar_autor(self, autorID):
        return self.__gestor_autores.buscar(autorID)

    # ============================================================
    #                       CATEGORÍAS
    # ============================================================

    def registrar_categoria(self, nombre):
        self.__validar_nombre(nombre)
        
        categorias = self.__gestor_categorias.listar()
        categoriaID = self.__generar_siguiente_id(categorias, 'categoriaID')
        categoria = Categoria(categoriaID, nombre.strip())
        self.__gestor_categorias.agregar(categoria)
        return categoria

    def eliminar_categoria(self, categoriaID):
        categoria = self.__gestor_categorias.buscar(categoriaID)
        if not categoria:
            raise BibliotecaError(f"No se encontró ninguna categoría con ID {categoriaID}.")

        if self.__gestor_libros.buscar_por_categoria(categoriaID):
            raise BibliotecaError("No se puede eliminar la categoría porque tiene libros asociados.")

        self.__gestor_categorias.eliminar(categoriaID)
        return categoria

    def listar_categorias(self):
        return self.__gestor_categorias.listar()

    def buscar_categoria(self, categoriaID):
        return self.__gestor_categorias.buscar(categoriaID)

    # ============================================================
    #                          LIBROS
    # ============================================================

    def registrar_libro(self, titulo, autorID, categoriaID, fechaPublicacion):
        if not titulo or not titulo.strip():
            raise BibliotecaError("El título no puede estar vacío.")

        if not self.__gestor_autores.buscar(autorID):
            raise BibliotecaError(f"No se encontró el autor con ID {autorID}.")

        if not self.__gestor_categorias.buscar(categoriaID):
            raise BibliotecaError(f"No se encontró la categoría con ID {categoriaID}.")

        self.__validar_fecha(fechaPublicacion)

        libros = self.__gestor_libros.listar()
        libroID = self.__generar_siguiente_id(libros, 'libroID')
        libro = Libro(libroID, titulo.strip(), autorID, categoriaID, fechaPublicacion)
        self.__gestor_libros.agregar(libro)
        return libro

    def eliminar_libro(self, libroID):
        libro = self.__gestor_libros.buscar(libroID)
        if not libro:
            raise BibliotecaError(f"No se encontró ningún libro con ID {libroID}.")

        if self.__gestor_prestamos.tiene_prestamo_activo(libroID):
            raise BibliotecaError("No se puede eliminar un libro que está actualmente prestado.")

        self.__gestor_libros.eliminar(libroID)
        return libro

    def listar_libros(self):
        return self.__gestor_libros.listar()

    def listar_libros_disponibles(self):
        return self.__gestor_libros.listar_disponibles()

    def buscar_libro(self, libroID):
        return self.__gestor_libros.buscar(libroID)

    # ============================================================
    #                          SOCIOS
    # ============================================================

    def registrar_socio(self, nombre, apellido, dni):
        self.__validar_nombre(nombre)
        self.__validar_nombre(apellido)
        self.__validar_dni(dni)

        if self.__gestor_socios.buscar_por_dni(dni):
            raise BibliotecaError(f"Ya existe un socio con DNI {dni}.")

        socios = self.__gestor_socios.listar()
        socioID = self.__generar_siguiente_id(socios, 'socioID')
        socio = Socio(socioID, nombre.strip(), apellido.strip(), dni)
        self.__gestor_socios.agregar(socio)
        return socio

    def desactivar_socio(self, socioID):
        socio = self.__gestor_socios.buscar(socioID)
        if not socio:
            raise BibliotecaError(f"No se encontró ningún socio con ID {socioID}.")

        if not socio.activo:
            raise BibliotecaError(f"El socio '{socio.nombre} {socio.apellido}' ya está inactivo.")

        if self.__gestor_prestamos.listar_por_socio(socioID):
            if any(not p.devuelto for p in self.__gestor_prestamos.listar_por_socio(socioID)):
                raise BibliotecaError("No se puede desactivar un socio con préstamos activos.")

        socio.desactivar()
        return socio

    def activar_socio(self, socioID):
        socio = self.__gestor_socios.buscar(socioID)
        if not socio:
            raise BibliotecaError(f"No se encontró ningún socio con ID {socioID}.")

        if socio.activo:
            raise BibliotecaError(f"El socio '{socio.nombre} {socio.apellido}' ya está activo.")

        socio.activar()
        return socio

    def listar_socios(self):
        return self.__gestor_socios.listar()

    def listar_socios_activos(self):
        return self.__gestor_socios.listar_activos()

    def buscar_socio(self, socioID):
        return self.__gestor_socios.buscar(socioID)

    # ============================================================
    #                        PRÉSTAMOS
    # ============================================================

    def prestar_libro(self, socioID, libroID):
        socio = self.__gestor_socios.buscar(socioID)
        if not socio:
            raise BibliotecaError(f"No se encontró el socio con ID {socioID}.")

        if not socio.activo:
            raise BibliotecaError(f"El socio '{socio.nombre} {socio.apellido}' está inactivo.")

        libro = self.__gestor_libros.buscar(libroID)
        if not libro:
            raise BibliotecaError(f"No se encontró el libro con ID {libroID}.")

        if not libro.disponible:
            raise BibliotecaError(f"El libro '{libro.titulo}' no está disponible.")

        prestamos = self.__gestor_prestamos.listar()
        prestamoID = self.__generar_siguiente_id(prestamos, 'prestamoID')
        prestamo = Prestamo(prestamoID, socioID, libroID)
        self.__gestor_prestamos.agregar(prestamo)
        libro.prestar()
        return prestamo

    def devolver_libro(self, prestamoID):
        prestamo = self.__gestor_prestamos.buscar(prestamoID)
        if not prestamo:
            raise BibliotecaError(f"No se encontró el préstamo con ID {prestamoID}.")

        if prestamo.devuelto:
            raise BibliotecaError("Este préstamo ya fue devuelto anteriormente.")

        prestamo.marcar_devuelto()

        libro = self.__gestor_libros.buscar(prestamo.libroID)
        if libro:
            libro.devolver()
        
        return prestamo

    def listar_prestamos(self):
        return self.__gestor_prestamos.listar()

    def listar_prestamos_activos(self):
        return self.__gestor_prestamos.listar_activos()

    def listar_prestamos_por_socio(self, socioID):
        return self.__gestor_prestamos.listar_por_socio(socioID)

    def buscar_prestamo(self, prestamoID):
        return self.__gestor_prestamos.buscar(prestamoID)

    # ============================================================
    #                    MÉTODOS DE CONSULTA
    # ============================================================

    def obtener_info_prestamo(self, prestamoID):
        prestamo = self.__gestor_prestamos.buscar(prestamoID)
        if not prestamo:
            return None

        socio = self.__gestor_socios.buscar(prestamo.socioID)
        libro = self.__gestor_libros.buscar(prestamo.libroID)

        return {
            'prestamo': prestamo,
            'socio': socio,
            'libro': libro
        }
