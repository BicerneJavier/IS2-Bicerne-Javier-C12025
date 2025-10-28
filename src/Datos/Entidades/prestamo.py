from datetime import date

class Prestamo:
    def __init__(self, prestamoID, socioID, libroID, fecha_prestamo=None, fecha_devolucion=None, devuelto=False):
        self.prestamoID = prestamoID
        self.socioID = socioID
        self.libroID = libroID
        self.fecha_prestamo = fecha_prestamo if fecha_prestamo is not None else date.today()
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = devuelto

    def marcar_devuelto(self):
        self.devuelto = True
        self.fecha_devolucion = date.today()
    
    def esta_activo(self):
        return not self.devuelto
    
    def __str__(self):
        estado = 'Devuelto' if self.devuelto else 'Pendiente'
        return f"PréstamoID: {self.prestamoID} - LibroID: {self.libroID} - SocioID: {self.socioID} - Estado: ({estado})"
    
    def __repr__(self):
        return f"Prestamo(id={self.prestamoID}, socioID={self.socioID}, libroID={self.libroID}, devuelto={self.devuelto})"