class Coordenada:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
        coord1 = Coordenada(3,30)
        coord2 = Coordenada(2,8)

        print("la distancia de la coordenada uno a la coordenada 2 es de :",coord1.distancia(coord2))
        print("La variable coordenada es instancia de la clase coordenada:",isinstance(coord2,Coordenada))
