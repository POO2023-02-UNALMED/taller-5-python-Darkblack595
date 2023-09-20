class Animal:
    _totalAnimales = 0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
        self.zona = None
    
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
    
    def getZona(self):
        return self._zona
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return "Mamifero: "+str(Mamifero.cantidadMamiferos())+"\nAves: "+str(Ave.cantidadAves())+"\nReptiles: "+str(Reptil.cantidadReptiles())+"\nPeces: "+str(Pez.cantidadPeces())+"\nAnfibios: "+str(Anfibio.cantidadAnfibios())
    
    def toString(self):
        return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self._habitat+" y mi genero es "+self._genero
    
    def movimiento(self):
        return "desplazarse"
