class Person:
    def __init__(self, name: str, last_name: str, sex: str, age: int,
                height: float, weight: float):
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_last_name(self) -> str:
        return self.last_name

    def set_last_name(self, last_name: str):
        self.last_name = last_name

    def get_sex(self) -> str:
        return self.sex

    def set_sex(self, sex: str):
        self.sex = sex

    def get_age(self) -> int:
        return self.age

    def set_age(self, age: int):
        self.age = age

    def get_height(self) -> float:
        return self.height

    def set_height(self, height: float):
        self.height = height

    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, weight: float):
        self.weight = weight

    def __str__(self):
        return (f"Nombre: {self.name}, apellido: {self.last_name}, sexo: {self.sex}, "
                f"edad: {self.age}, altura: {self.height} mts, peso: {self.weight} kg")


person_1 = Person("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
person_2 = Person("Juan", "Camargo", "Masculino", 18, 1.8, 75)

print("")
print(f"Persona 1 original:", person_1)
person_1.set_age(21)
print(f"Persona 1 modificada:", person_1)
print(f"Persona 2 original:", person_2)
person_2.set_last_name("Santiago")
print(f"Persona 2 modificada:", person_2)
print("")