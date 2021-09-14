class DispositivoMovil():

    def __init__(self, marca, color):
        self._marca = marca # Con un raya al piso es variable protegida
        self._color = color

    def darMarca(self):
        return self._marca

    def darColor(self):
        return self._color

class Celular(DispositivoMovil):

    def __init__(self, numero, marca, color):
        super().__init__(marca, color)
        self.__numero = numero

    @property
    def numero(self):
        return self.__numero



cel = Celular(3112727922, "iPhone", "Black")
print(cel._color)
print(cel.darColor())