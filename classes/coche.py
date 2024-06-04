class Coche:
    marca = ""
    modelo = ""
    __encendido = False # Encapsulamiento

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        self.__encendido = True

    def apagar(self):
        self.__encendido = False

    def esta_encendido(self):
        return self.__encendido

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
class CocheElectrico(Coche):
    bateria = 0
    
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = bateria

    def __str__(self):
        return f"{super().__str__()}, Batería: {self.bateria} kWh"