class Asiento():
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        valoresPermitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        for i in valoresPermitidos:
            if color == i:
                self.color = color

class Auto():
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        cantidadAsientos = 0
        for i in self.asientos:
            if type(i) == Asiento:
                cantidadAsientos += 1
        return cantidadAsientos
    def verificarIntegridad(self):
        for i in self.asientos:
            if type(i) == Asiento:
                if self.registro == self.motor.registro and self.registro == i.registro:
                    return "Auto original"
                else:
                    return "Las piezas no son originales"


class Motor():
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros =numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if tipo ==  "electrico":
            self.tipo = tipo
        if tipo ==  "gasolina":
            self.tipo = tipo