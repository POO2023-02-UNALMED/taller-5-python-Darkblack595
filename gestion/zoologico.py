from gestion.zona import Zona
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
    def getZona(cls):
        return cls._zonas
    
    @classmethod
    def cantidadTotalAnimales(cls):
        zoototal = 0
        for i in range(0,len(cls._zonas)-1,1):
            zoototal += cls._zonas[i].cantidadAnimales()
        return zoototal

    @classmethod
    def agregarZonas(cls,zona):
        cls._zonas.append(zona)