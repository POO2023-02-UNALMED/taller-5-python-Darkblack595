from zooAnimales.animal import Animal
class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    totalAnfibios = 0
    def __init__(self,nombre = None,edad = None,habitat = None,genero = None,colorPiel = None,venenoso = None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        Anfibio.totalAnfibios += 1

    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,colorPiel):
        self._colorPiel = colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self,venenoso):
        self._venenoso = venenoso
    
    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def crearRana(cls,nombre,edad,genero):
        rana = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        ranas += 1
        cls._listado.append(rana)
        return rana
    
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        salamandras += 1
        cls._listado.append(salamandra)
        return salamandra
    
    @classmethod
    def cantidadAnfibios(cls):
        return cls.totalAnfibios
