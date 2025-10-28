from .gestor_base import GestorBase

class GestorPrestamos(GestorBase):
    def buscar(self, prestamoID):
        return self._buscar_por_atributo('prestamoID', prestamoID)

    def eliminar(self, prestamoID):
        self._eliminar_por_atributo('prestamoID', prestamoID)

    def listar_por_socio(self, socioID):
        return self._listar_por_atributo('socioID', socioID)

    def listar_por_libro(self, libroID):
        return self._listar_por_atributo('libroID', libroID)

    def listar_activos(self):
        return [p for p in self._elementos if not p.devuelto]

    def tiene_prestamo_activo(self, libroID):
        return any(p.libroID == libroID and not p.devuelto for p in self._elementos)
