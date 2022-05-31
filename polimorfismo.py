class persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('soy ' + self.nombre + ' y estoy caminando')
    
class ciclista(persona):
    def avanza(self):
        print('soy ' + self.nombre + ' y estoy andando en bicicleta')


def main():

    andres = persona("andres")
    pedro = ciclista("pedro")
    andres.avanza()
    pedro.avanza()
   


if __name__ == "__main__":
    main()