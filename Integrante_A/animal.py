class animal:
    def __init__(self, name, surname, age, height, weight, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
        self.sex = sex

    def to_dict(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'sex': self.sex
            }

    def getName(self):
        return  self.name

    def getName(self, name):
        self.name = name

    def getSurname(self):
        return  self.surname

    def getSurname(self, surname):
        self.surname =surname

    def getAge(self):
        return self.age

    def getAge(self, age):
        self.age = age

    def getHeight(self):
        return self.height

    def getHeight(self, height):
        self.height = height

    def getWeight(self):
        return self.weight

    def getWeight(self, weight):
        self.weight = weight

    def getSex(self):
        return self.sex

    def getSex(self, sex):
        self.sex = sex

    def animal1(self):
        print("el meu nom: " + self.name)
        print("el meu cognom: " + self.surname)
        print("la meva edad: " + self.age)
        print("el meu pes: " + self.weight)
        print("la meva altura: " + self.height)
        print("el meu sexe es: " + self.sex)
