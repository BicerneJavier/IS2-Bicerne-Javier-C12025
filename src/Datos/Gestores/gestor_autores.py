from .gestor_base import GestorBase

class GestorAutores(GestorBase):
    def buscar(self, autorID):
        return self._buscar_por_atributo('autorID', autorID)

    def eliminar(self, autorID):
        self._eliminar_por_atributo('autorID', autorID)