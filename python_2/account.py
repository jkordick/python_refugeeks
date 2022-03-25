class Account:
    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.id) + ': ' + str(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance
    
    def setBalance(self, balance):
        self.balance = balance

    # Schreibe einen get-Methode und eine set-Methode 
    # für die Attribute/Variablen name und id
    # Achtet auf die Namenskonventionen!

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id
    
    def setId(self):
        self.id = id

newAccount = Account('Julia', 1337, 100.00)
print(newAccount.getBalance())
newAccount.setBalance(1000.00)
print(newAccount.getBalance())











