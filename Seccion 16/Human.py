class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __add__(self, other):
        if(isinstance(other, Human)):
            age = self.age + other.age
            name = f'{self.name}{other.name}'
            return (f'Age: {age} , Name: {name}')

    def __sub__(self, other):
        if(isinstance(other, Human)):
            age = self.age - other.age
            return f'Substraccion age: {age}'


obj1 = Human('Agustin', 18)
obj2 = Human('Nacho', 6)


suma = obj1 + obj2
resta = obj2 - obj1
print(suma)
print(resta)

# obj1 + obj2 en realidad es obj1.add(obj2)
