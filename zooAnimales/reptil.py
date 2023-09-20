class Reptil:
    _listado = []
    iguanas = 0
    serpientes = 0
    totalReptiles = 0
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)
        totalReptiles += 1
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,largoCola):
        self._largoCola = largoCola
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        iguana = Reptil(nombre,edad,"humedal",genero,"verde",3)
        iguanas += 1
        cls._listado.append(iguana)
        return iguana

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        serpiente = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        serpientes += 1
        cls._listado.append(serpiente)
        return serpiente

    @classmethod
    def cantidadReptiles(cls):
        return cls.totalReptiles