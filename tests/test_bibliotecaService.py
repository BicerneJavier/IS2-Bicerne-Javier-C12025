import unittest

from src.Negocio.bibliotecaService import BibliotecaService, BibliotecaError
from src.Datos.Gestores.gestor_base import GestorBase

class TestBibliotecaService(unittest.TestCase):

    def setUp(self):
        """
        Este método se ejecuta antes de cada prueba.
        Limpia el estado de los singletons y crea una nueva instancia de BibliotecaService
        para asegurar que las pruebas estén aisladas.
        """
        # Limpiar todas las instancias de gestores antes de cada prueba
        GestorBase._reset_singleton_for_testing()
        
        self.servicio = BibliotecaService()
        # Registrar algunas entidades básicas para las pruebas
        self.autor = self.servicio.registrar_autor("Gabriel", "García Márquez")
        self.categoria = self.servicio.registrar_categoria("Novela")
        self.socio = self.servicio.registrar_socio("Javier", "Bicerne", "12345678")

    def test_registrar_autor(self):
        """Prueba que se pueda registrar un autor correctamente."""
        autor = self.servicio.registrar_autor("Julio", "Cortázar")
        self.assertIsNotNone(autor)
        self.assertEqual(autor.nombre, "Julio")
        self.assertEqual(autor.apellido, "Cortázar")
        self.assertIn(autor, self.servicio.listar_autores())

    def test_registrar_libro(self):
        """Prueba el registro exitoso de un libro."""
        libro = self.servicio.registrar_libro(
            "Cien años de soledad",
            self.autor.autorID,
            self.categoria.categoriaID,
            "1967-05-30"
        )
        self.assertIsNotNone(libro)
        self.assertEqual(libro.titulo, "Cien años de soledad")
        self.assertIn(libro, self.servicio.listar_libros())

    def test_prestar_libro_exitosamente(self):
        """Prueba que un socio activo pueda tomar prestado un libro disponible."""
        libro = self.servicio.registrar_libro(
            "Rayuela",
            self.autor.autorID,
            self.categoria.categoriaID,
            "1963-06-28"
        )
        
        prestamo = self.servicio.prestar_libro(self.socio.socioID, libro.libroID)
        
        self.assertIsNotNone(prestamo)
        self.assertFalse(libro.disponible, "El libro debería marcarse como no disponible después del préstamo.")
        self.assertIn(prestamo, self.servicio.listar_prestamos_activos())

    def test_prestar_libro_no_disponible(self):
        """Prueba que no se puede prestar un libro que ya está prestado."""
        libro = self.servicio.registrar_libro("El túnel", self.autor.autorID, self.categoria.categoriaID, "1948-01-01")
        
        # Primer préstamo (exitoso)
        self.servicio.prestar_libro(self.socio.socioID, libro.libroID)
        
        # Intentar prestar el mismo libro de nuevo
        with self.assertRaisesRegex(BibliotecaError, "no está disponible"):
            self.servicio.prestar_libro(self.socio.socioID, libro.libroID)

    def test_devolver_libro(self):
        """Prueba la devolución exitosa de un libro."""
        libro = self.servicio.registrar_libro("Ficciones", self.autor.autorID, self.categoria.categoriaID, "1944-01-01")
        prestamo = self.servicio.prestar_libro(self.socio.socioID, libro.libroID)
        
        self.assertFalse(libro.disponible) # Verificar que no está disponible
        
        prestamo_devuelto = self.servicio.devolver_libro(prestamo.prestamoID)
        
        self.assertTrue(prestamo_devuelto.devuelto)
        self.assertTrue(libro.disponible, "El libro debería estar disponible después de la devolución.")

    def test_eliminar_autor_con_libros_asociados(self):
        """Prueba que no se puede eliminar un autor si tiene libros registrados."""
        self.servicio.registrar_libro("El Aleph", self.autor.autorID, self.categoria.categoriaID, "1949-01-01")
        
        with self.assertRaisesRegex(BibliotecaError, "libros asociados"):
            self.servicio.eliminar_autor(self.autor.autorID)

    def test_eliminar_categoria_con_libros_asociados(self):
        """Prueba que no se puede eliminar una categoría si tiene libros registrados."""
        self.servicio.registrar_libro("Bestiario", self.autor.autorID, self.categoria.categoriaID, "1951-01-01")
        
        with self.assertRaisesRegex(BibliotecaError, "libros asociados"):
            self.servicio.eliminar_categoria(self.categoria.categoriaID)

if __name__ == '__main__':
    unittest.main()
