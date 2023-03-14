class car:
    def __init__(self, material, modelo, año, color, numRuedas, maxVelocidad):
        self.material = material
        self.modelo = modelo
        self.año = año
        self.color = color
        self.num_ruedas = numRuedas
        self.max_velocidad = maxVelocidad

    def to_dict(self):
        return {
            "material": self.material,
            "modelo": self.modelo,
            "año": self.año,
            "color": self.color,
            "num_ruedas": self.num_ruedas,
            "max_velocidad": self.max_velocidad
        }
    def getMaterial(self):
        return self.material

    def setMaterial(self, material):
        self.material = material

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getAño(self):
        return self.año

    def setAño(self, año):
        self.año = año

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getNumRuedas(self):
        return self.num_ruedas

    def setNumRuedas(self, num_ruedas):
        self.num_ruedas = num_ruedas

    def getMaxVelocidad(self):
        return self.max_velocidad

    def setMaxVelocidad(self, max_velocidad):
        self.max_velocidad = max_velocidad

    def partes(self):
        print("Material:", self.material)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Color:", self.color)
        print("Numero de ruedas:", self.num_ruedas)
        print("Max Velocidad:", self.max_velocidad)
