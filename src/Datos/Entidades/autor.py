class Autor:
    def __init__(self, autorID, nombre, apellido):
        self.autorID = autorID
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"ID: {self.autorID} - {self.nombre} {self.apellido}"
    
    def __repr__(self):
        return f"Autor(id={self.autorID}, nombre='{self.nombre}', apellido='{self.apellido}')"
