from animal import Animal
class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    totalmamiferos = 0
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        totalmamiferos += 1
    def __init__(self):
        super().__init__("",0,"","")
        Mamifero._listado.append(self)
        totalmamiferos += 1

    def getPelaje(self):
        return self._pelaje
    def setPelaje(self,pelaje):
        self._pelaje = pelaje
    
    def getPatas(self):
        return self._patas
    def setPatas(self,patas):
        self._patas = patas
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def crearCaballos(cls,nombre,edad,genero):
        caballo = Mamifero(nombre,edad,"pradera",genero,True,4)
        caballos += 1
        cls._listado.append(caballo)
        return caballo
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        leon = Mamifero(nombre,edad,"selva",genero,True,4)
        leones += 1
        cls._listado.append(leon)
        return leon
    
    @classmethod
    def cantidadMamiferos(cls):
        return cls.totalMamiferos