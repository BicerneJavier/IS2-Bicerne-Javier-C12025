from .gestor_base import GestorBase

class GestorCategorias(GestorBase):
    def buscar(self, categoriaID):
        return self._buscar_por_atributo('categoriaID', categoriaID)

    def eliminar(self, categoriaID):
        self._eliminar_por_atributo('categoriaID', categoriaID)