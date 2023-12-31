from zooAnimales.animal import Animal
class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    totalAves = 0
    def __init__(self,nombre = None,edad  =  None,habitat = None,genero = None,colorPlumas = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
        Ave.totalAves += 1

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas = colorPlumas
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon = Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        cls.halcones += 1
        cls._listado.append(halcon)
        return halcon
    
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        aguila = Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        cls.aguilas += 1
        cls._listado.append(aguila)
        return aguila
    
    @classmethod
    def cantidadAves(cls):
        return cls.totalAves
    
    def movimiento(self):
        return "volar"