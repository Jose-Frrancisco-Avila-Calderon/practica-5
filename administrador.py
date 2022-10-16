
from particula import Particula
from algoritmos import distancia_euclidiana
class administrador:
    def __init__(self):
        self.__particulas = []
    def  agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

      
p01 = Particula(id= "1", origen_x= "2", origen_y= "3", destino_x= "4", destino_y= "5", velocidad="6", red= "7", green="8", blue="9", distancia=distancia_euclidiana)
p02 = Particula(id= "2", origen_x= "3", origen_y= "3", destino_x= "4", destino_y= "5", velocidad="6", red= "7", green="8", blue="9", distancia=distancia_euclidiana)

particula = administrador() 
particula.agregar_final(p01)
particula.agregar_inicio(p02)

particula.mostrar()
