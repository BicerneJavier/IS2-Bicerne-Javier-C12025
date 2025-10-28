class GestorBase:
    #Clase base genérica para gestionar una colección de elementos en memoria.
    #Implementa el patrón Singleton para asegurar una única instancia por gestor.
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    #Seria asi: GestorBase._instances == {GestorLibros: <objeto>, GestorAutores: <objeto>}

    def __init__(self):
        # Evita la reinicialización de la instancia. (Que solo exista una única instancia)
        if hasattr(self, '_initialized'):
            return
        self._elementos = []
        self._initialized = True

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def listar(self):
        return self._elementos

    def _buscar_por_atributo(self, attr_nombre, valor):
        for e in self._elementos:
            if getattr(e, attr_nombre) == valor:
                return e
        return None

    def _eliminar_por_atributo(self, attr_nombre, valor):
        self._elementos = [e for e in self._elementos if getattr(e, attr_nombre) != valor]

    def _listar_por_atributo(self, attr_nombre, valor):
        return [e for e in self._elementos if getattr(e, attr_nombre) == valor]

    @classmethod
    def _reset_singleton_for_testing(cls):
        # Limpia todas las instancias de singletons para los tests
        cls._instances = {}