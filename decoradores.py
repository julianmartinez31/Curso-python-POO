class humano:
    def __init__(self,edad,genero,nacional,ocupacion):
        self.edad = edad
        self.genero = genero
        self.nacional = nacional
        self._ocupacion = ocupacion
        self._c_social = None
        self._oportunidades = None

class Educacion:
    def __init(self,nivel,curiosidad):
        self.nivel = nivel
        self.curiosidad = curiosidad
        if nivel == "profesional" and curiosidad == "alta":
            self._proyeccion = "Muy favorable"
        elif nivel != "profesional" and curiosidad == "alta":
            self._proyeccion = "favorable"
        elif nivel == "profesional" and curiosidad == "baja":
            self._proyeccion = "mediocre"

