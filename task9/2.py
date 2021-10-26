class Pet():
    def __init__(self, name, type, years, sound):
        self.name = name
        self._type = type
        self._years = years
        self.sound = sound


class Dog(Pet):
    def sound(self):
        print(self.sound())
        
    def show(self):
        print(self.name)
        
    def type(self):
        print(self._type)
        
    def years(self):
        print(self._years)

class Cat(Pet):
    def sound(self):
        print(self.sound())

    def show(self):
        print(self.name)

    def type(self):
        print(self._type)

    def years(self):
        print(self._years)
