from typing import final


class BalanceLowException(Exception):
    def __str__(self):
        return "Balance of Account to low to withdraw balance!"

class Account:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.balance = 0.0

    def __str__(self):
        return str(self.name) + ' ' + str(self.id) + ': ' + str(self.balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise BalanceLowException()
        else:
            self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def getBalance(self):
        return self.balance

    

# Auf Exception reagieren
try:
    acc = Account("Max", 0)
    acc.deposit(500)
    acc.withdraw(1000) # Fehler wird hier geworfen
except BalanceLowException as b_low_e:
    print(b_low_e) # __str__ wird ausgeführt



# Auf Exception reagieren
# try:
#     input = int(input("Eine Zahl eingeben größer 0 eingeben: "))
#     print(5 / input)
# except ZeroDivisionError:
#     print("Fehler: die Eingabe darf nicht 0 sein")
# finally: # wird immer ausgeführt
#     print("Fertig")