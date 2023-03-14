import json

from Integrante_A.car import car
from Integrante_A.animal import animal

animals = [
    animal("Rufus", "González", 3, 60, 20, "Macho"),
    animal("Mittens", "Smith", 2, 30, 5, "Hembra"),
    animal("Thunder", "Johnson", 5, 160, 500, "Macho"),
    animal("Thumper", "Jones", 1, 20, 1, "Macho"),
    animal("Tweety", "García", 2, 10, 0.5, "Hembra")
]

cars = [
    car("Fibra de carbono", "Lamborghini Huracán", 2022, "Rojo", 4, 350),
    car("Acero", "Toyota Yaris", 2021, "Blanco", 4, 200),
    car("Acero", "Volvo VNL 760", 2019, "Azul", 6, 110),
    car("Acero", "Ford Transit", 2017, "Gris", 4, 120),
    car("Fibra de carbono", "Ducati Panigale V4", 2020, "Negro", 2, 300)
]

animals_dict_list = [animal.to_dict() for animal in animals]
cars_dict_list = [car.to_dict() for car in cars]

data = {
    "animals": animals_dict_list,
    "cars": cars_dict_list
}
with open("jsonAPI/a.json", 'w') as file:
    json.dump(data, file)
