class Socio:
    def __init__(self, socioID, nombre, apellido, dni, activo=True):
        self.socioID = socioID
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.activo = activo

    def desactivar(self):
        self.activo = False

    def activar(self):
        self.activo = True

    def __str__(self):
        estado = 'Activo' if self.activo else 'Inactivo'
        return f"ID: {self.socioID} - {self.nombre} {self.apellido} - DNI: {self.dni} ({estado})"
    
    def __repr__(self):
        return f"Socio(id={self.socioID}, nombre='{self.nombre}', apellido='{self.apellido}', dni='{self.dni}', activo={self.activo})"
