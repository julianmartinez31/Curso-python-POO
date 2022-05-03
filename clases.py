# definicion de clase 

class nombre_de_la_clase(super_clase):

    # a toda funcion dentro de una clase se le llama metodo
    def __init__(self, parametros):
        pass
        #expresiones del metodo

# EJEMPLO

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre, me llamo {self.nombre}.'
        
         