class Person: # Parent, Parentclass, Elternklasse, Superklasse
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        return str(self.name) + ' ' + str(self.alter)

class Studierende(Person): # Kinderklassen oder Subklassen, Children
    def __init__(self, name, alter, studi_id):
        super().__init__(name, alter) # Aufruf des Konstruktors der Eltern bzw Superklasse.
        self.studi_id = studi_id

    def __str__(self):
        return str(super().__str__()) + ' ' + str(self.studi_id)

class Dozierende(Person):
    def __init__(self, name, alter, dozi_id):
        super().__init__(name, alter)
        self.dozi_id = dozi_id

studi = Studierende(12345)
print(studi)

person = Person('Julia', 31)