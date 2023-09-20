from zooAnimales.animal import Animal
class Zona:
    _animales = []
    def __init__(self,nombre ,zoo=None):
        self._nombre = nombre
        self._zoo = zoo
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getZoo(self):
        return self._zoo
    def setZoo(self,zoo):
        self._zoo = zoo
    
    @classmethod
    def getAnimales(cls):
        return cls._animales
    
    @classmethod
    def agregarAnimales(cls,animal):
        cls._animales.append(animal)
    
    @classmethod
    def cantidadAnimales(cls):
        total = 0
        for animal in cls._animales:
            total += 1  
        return total