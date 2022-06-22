class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self) -> str:
        return f"Car name is {self.name} and model is {self.model}"

    def __repr__(self) -> object:
        return f"Object of {type(self)}: {self.__module__}, Current details {self.name}-{self.model} "


mycar = Car("Audi", "Q4 e-tron")
print(mycar.__str__())
print(mycar.__repr__())
