# Falsch!
["Max", 22424, 52.23]  # name, id, kontostand

# Richtig


class Account:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.balance = 0.0

    def __str__(self):
        return str(self.name) + ' ' + str(self.id) + ': ' + str(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def getBalance(self):
        return self.balance


# Objekte erzeugen
acc1 = Account("Max", 22424)
acc2 = Account("Julia", 22425)

# Methoden aufrufen
acc1.deposit(500)
print(acc1.getBalance())  # 500
acc2.deposit(250)
acc2.deposit(105)
print(acc2)  # Julia 22425: 355.0

# direkter aufruf von balance
acc = Account("Max", 22424)
acc.balance = 2500
print(acc.getBalance())

# private attributes


class PrivateAccount:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__balance = 0.0


# acc_private = PrivateAccount("Max", 22426)
# print(acc_private.__name)  # AttributeError


# Vererbung
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print(self.name, self.age)


max = Person("Max", 20)
max.printinfo() # Max 20

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def printinfo(self):
        print(self.name, self.age, self.id)

max = Student("Max", 20, 1000)
max.printinfo() # Max 20 1000
