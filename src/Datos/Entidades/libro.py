class Libro:
    def __init__(self, libroID, titulo, autorID, categoriaID, fechaPublicacion, disponible=True):
        self.libroID = libroID
        self.titulo = titulo
        self.autorID = autorID
        self.categoriaID = categoriaID
        self.fechaPublicacion = fechaPublicacion
        self.disponible = disponible
        
    def prestar(self):
        self.disponible = False
    
    def devolver(self):
        self.disponible = True

    def __str__(self):
        estado = 'Disponible' if self.disponible else 'Prestado'
        return f"{self.libroID} - {self.titulo} ({estado})"
    
    def __repr__(self):
        return f"Libro(id={self.libroID}, titulo='{self.titulo}', autorID={self.autorID}, categoriaID={self.categoriaID}, disponible={self.disponible})"
