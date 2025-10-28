class Categoria:
    def __init__(self, categoriaID, nombre):
        self.categoriaID = categoriaID
        self.nombre = nombre

    def __str__(self):
        return f"{self.categoriaID} - {self.nombre}"
    
    def __repr__(self):
        return f"Categoria(id={self.categoriaID}, nombre='{self.nombre}')"
