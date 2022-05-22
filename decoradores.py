class humano:
    def __init__(self,edad,genero,nacional,ocupacion):
        self.edad = edad
        self.genero = genero
        self.nacional = nacional
        self._ocupacion = ocupacion
        self._c_social()
        self._oportunidades()
        self._educacion = Educacion("profesional", "alta")


class Educacion:
    def __init__(self,nivel,curiosidad):
        self.nivel = nivel
        self.curiosidad = curiosidad
        if nivel == "profesional" and curiosidad == "alta":
            self._proyeccion = "Muy favorable"
        elif nivel != "profesional" and curiosidad == "alta":
            self._proyeccion = "favorable"
        elif nivel == "profesional" and curiosidad == "baja":
            self._proyeccion = "mediocre"

if __name__ == "__main__":

    humano(25,"hombre","colombiana","ingeniero")