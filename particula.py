from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id= 0,  origen_x= 0, origen_y= 0, destino_x= 0, destino_y= 0, velocidad= 0, red= 0, green= 0, blue= 0, distancia= 0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia= distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)
    def __str__(self):
        return(
            'id: ' + str(self.__id) +'\n'
            'origen x ' + str(self.__origen_x) + '\n'
            'origen y ' + str(self.__origen_y) + '\n'
            'destino x ' + str(self.__destino_x) + '\n'
            'destino y ' + str(self.__destino_y) + '\n'
            'velocidad ' + str(self.__velocidad) + '\n'
            'red ' + str(self.__red) + '\n'
            'green ' + str(self.__green) + '\n'
            'blue ' + str(self.__blue) + '\n'
            'distancia ' + str(self.__distancia) + '\n'
        )

