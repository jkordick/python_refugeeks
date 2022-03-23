# Wir schreiben einen Passwort-Manager


































# Schreibe eine Klasse Account mit den drei Attributen
# program - das Programm, zu dem der Account gehört
# username - der Benutzername, der zum Zugang zu dem Programm verwendet wird
# password - das Passwort, das zum Zugang zu dem Programm verwendet wird
# und zwei Methoden/Funktionen:
# getProgramName() - die das zugehörige Program des Accounts zurück gibt
# changePassword(password) - um das gespeicherte Passwort zu ändern

from re import U


class Account:
    def __init__(self, program, username, password, istAdminAccount):
        self.program = program
        self.__username = username
        self.__password = password
        self.istAdminAccount = istAdminAccount
    
    def __str__(self):
        return str(self.program) + ', ' + str(self.__username) + ', ' + str(self.__password)
    
    def getProgramName(self):
        return self.program
    
    def __setPassword__(self, password):
        self.__password = password
    
    def changePassword(self, neues_password):
        self.__setPassword__(neues_password)
    
    def setProgram(self, program):
        self.program = program
    
    def __getUsername__(self):
        return self.__username
    
    def __setUsername__(self, username):
        self.__username = username
    
    def getIstAdminAccount(self):
        return self.istAdminAccount


# Schreibe eine Klasse AdminAccount, die von Account erbt.
# AdminAccount hat ein zusätzliches Attribut
# istAdminAcccount - boolean
# Überlege dir, wie man den AdminAccount besonders gegen die 
# Manipulierung von Daten schützen sollte!
# Es darf nur ein AdminAccount erstellt werden.
# Überlege dir, wie man die Erstellung eines weiteren AdminAccounts verhindern
# könnte - Exception?

class AdminAccountException(Exception):
    def __str__(self):
        return "Es darf nur ein Admin Account erstellt werden"
class AdminAccount(Account):
    i = 0
    def __init__(self, program, username, password):
        AdminAccount.i += 1
        if AdminAccount.i > 1:
            raise AdminAccountException()
        else:
            super().__init__(program, username, password, True)
            print(AdminAccount.i)
    
    def __str__(self):
        return Account.__str__(self)

# 1. Lösung: Verwalten alle unsere Account, also Account & AdminAccount in einer Liste
# und prüfen, vor der Erstellung jedes Accounts, ob sich in der Liste bereits ein
# AdminAccount befindet. - hat geklappt, danke mohammad <3
# 2. Lösung: Wir zählen, wie viele AdminAccounts erstellt wurden und sobald versucht wird einen 
# weiteren AdminAccount zu erstellen, werfen wir unsere Exception.

accountList = []
acc0 = Account("SAP", "julia", 3312332, False)
accountList.append(acc0)
acc1 = Account("Webmail", "julia", 3312332, False)
accountList.append(acc1)
acc2 = AdminAccount("PasswortManager", "julia", 3312332)
accountList.append(acc2)

def pruefeAdminAccountBereitsVorhanden(program, username, password):
    for a in accountList:
        if a.getIstAdminAccount():
            raise AdminAccountException()
        else:
            return AdminAccount(program, username, password)

acc4 = pruefeAdminAccountBereitsVorhanden("PasswortManager", "julia", 3312332)


"""
try:
    acc2 = AdminAccount("PasswortManager", "julia", 3312332)
except:
    print(AdminAccountException())
finally:
    print("Hat geklappt")

try: 
    acc3 = AdminAccount("PasswortManager", "julia", 3312332)
except:
    print(AdminAccountException())
finally:
    print("Hat nicht geklappt")

"""









































# Schreibe eine Klasse PasswordManager mit zwei Attributen:
# adminAccount - vom Typ AdminAccount
# accounts - eine Liste mit Accounts
# und 4 Methoden:
# isPasswortValid(passwort) - gibt True oder False zurück
# addAccount(account) - selbsterklärend
# getAllAccounts() - gibt eine Liste aller Accounts zurück
# getAccount4Program(program) - gibt eine Liste aller Accounts zu einem bestimmten
# Programm zurück
