class Animal:
    _totalAnimales = 0
    _zona = []
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
    def __init__(self):
        Animal.totalAnimales += 1
    
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero = genero
    
    @classmethod
    def getZona(cls):
        return cls._zona
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def totalPorTipo(cls):
        from mamifero import Mamifero
        from ave import Ave
        from reptil import Reptil
        from pez import Pez
        from anfibio import Anfibio
        return "Mamifero: ",Mamifero.cantidadMamiferos,"\n","Aves: ",Ave.cantidadAves,"\n","Reptiles: ",Reptil.cantidadReptiles,"\n","Peces: ",Pez.cantidadPeces,"\n","Anfibios: ",Anfibio.cantidadAnfibios
    
    def toString(self):
        return "Mi nombre es ",self._nombre,", tengo una edad de ",self._edad,", habito en ",self._habitat," y mi genero es ",self._genero
    
