from .gestor_base import GestorBase

class GestorSocios(GestorBase):
    def buscar(self, socioID):
        return self._buscar_por_atributo('socioID', socioID)

    def buscar_por_dni(self, dni):
        return self._buscar_por_atributo('dni', dni)

    def eliminar(self, socioID):
        self._eliminar_por_atributo('socioID', socioID)

    def listar_activos(self):
        return [s for s in self._elementos if s.activo]
