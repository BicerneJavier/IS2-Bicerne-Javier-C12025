from .gestor_base import GestorBase

class GestorLibros(GestorBase):
    def buscar(self, libroID):
        return self._buscar_por_atributo('libroID', libroID)

    def buscar_por_autor(self, autorID):
        return self._listar_por_atributo('autorID', autorID)

    def buscar_por_categoria(self, categoriaID):
        return self._listar_por_atributo('categoriaID', categoriaID)

    def eliminar(self, libroID):
        self._eliminar_por_atributo('libroID', libroID)

    def listar_disponibles(self):
        return [l for l in self._elementos if l.disponible]
