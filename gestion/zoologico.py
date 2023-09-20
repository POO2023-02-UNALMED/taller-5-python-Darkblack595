class Zoologico:
    _zonas = []
    def __init__(self,nombre,ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self,ubicacion):
        self._ubicacion = ubicacion
    
    @classmethod
    def getZonas(cls):
        return cls._zonas
    
    @classmethod
    def cantidadTotalAnimales(cls):
        cantotalanimales = 0
        for i in range(0,len(cls._zonas),1):
            if cls._zonas[i].getnombre() == cls.getnombre():
                cantotalanimales += cls._zonas[i].cantidadAnimales()
        return cantotalanimales

    @classmethod
    def agregarZonas(cls,zona):
        cls._zonas.append(zona)