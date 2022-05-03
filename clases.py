# # definicion de clase 

# class nombre_de_la_clase(super_clase):

#     # a toda funcion dentro de una clase se le llama metodo
#     def __init__(self, parametros):
#         pass
#         #expresiones del metodo

# # EJEMPLO

#def run():

#     class Persona:
#         def __init__(self, nombre, edad):
#             self.nombre = nombre
#             self.edad = edad

#         def saluda(self, otra_persona):
#             return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'


#     david = Persona("david", 35)
#     erika = Persona("erika", 44)

#     print(david.saluda(erika))

class coordenada:

    def __init__(self,cordx,cordy):
        self.cordx = cordx
        self.cordy = cordy

    def diff(self,otra_cord):

        difx = (self.cordx - otra_cord.cordx)**2
        dify = (self.cordy - otra_cord.cordy)**2

        return  (difx + dify)**0.5
 
    

if __name__ == '__main__':
   
    punto1 = coordenada(3,30)
    punto2 = coordenada(4,8)

    print(str(punto1.diff(punto2)))

         