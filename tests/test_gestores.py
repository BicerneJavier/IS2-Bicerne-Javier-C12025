import unittest

from src.Datos.Gestores.gestor_libros import GestorLibros
from src.Datos.Entidades.libro import Libro
from src.Datos.Gestores.gestor_autores import GestorAutores
from src.Datos.Entidades.autor import Autor
from src.Datos.Gestores.gestor_base import GestorBase

class TestGestores(unittest.TestCase):

    def setUp(self):
        # Limpiar el estado de los singletons antes de cada prueba
        GestorBase._reset_singleton_for_testing()

    def test_gestor_autores(self):
        """Prueba las operaciones básicas del GestorAutores."""
        gestor = GestorAutores()
        autor = Autor(autorID=1, nombre="Jorge Luis", apellido="Borges")

        # Probar agregar
        gestor.agregar(autor)
        self.assertIn(autor, gestor.listar())

        # Probar buscar
        autor_encontrado = gestor.buscar(1)
        self.assertEqual(autor_encontrado, autor)

        # Probar eliminar
        gestor.eliminar(1)
        self.assertIsNone(gestor.buscar(1))
        self.assertNotIn(autor, gestor.listar())

    def test_gestor_libros(self):
        """Prueba las operaciones básicas del GestorLibros."""
        gestor = GestorLibros()
        libro = Libro(libroID=1, titulo="El Aleph", autorID=1, categoriaID=1, fechaPublicacion="1949-01-01")

        # Probar agregar
        gestor.agregar(libro)
        self.assertIn(libro, gestor.listar())

        # Probar buscar
        libro_encontrado = gestor.buscar(1)
        self.assertEqual(libro_encontrado, libro)

        # Probar búsqueda por autor y categoría
        self.assertTrue(gestor.buscar_por_autor(1))
        self.assertFalse(gestor.buscar_por_autor(99))
        self.assertTrue(gestor.buscar_por_categoria(1))
        self.assertFalse(gestor.buscar_por_categoria(99))

        # Probar eliminar
        gestor.eliminar(1)
        self.assertIsNone(gestor.buscar(1))

if __name__ == '__main__':
    unittest.main()
