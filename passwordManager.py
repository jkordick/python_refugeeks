# Wir schreiben einen Passwort-Manager


































# Schreibe eine Klasse Account mit den drei Attributen
# program - das Programm, zu dem der Account gehört
# username - der Benutzername, der zum Zugang zu dem Programm verwendet wird
# password - das Passwort, das zum Zugang zu dem Programm verwendet wird
# und zwei Methoden/Funktionen:
# getProgramName() - die das zugehörige Program des Accounts zurück gibt
# changePassword(password) - um das gespeicherte Passwort zu ändern

class Account:
    def __init__(self, program, username, password):
        self.program = program
        self.__username = username
        self.__password = password
    
    def __str__(self):
        return str(self.program) + ', ' + str(self.__username) + ', ' + str(self.__password)
    
    def getProgramName(self):
        return self.program
    
    def __setPassword__(self, password):
        self.__password = password
    
    def changePassword(self, password):
        self.__setPassword__(password)
    
    def setProgram(self, program):
        self.program = program
    
    def __getUsername__(self):
        return self.__username
    
    def __setUsername__(self, username):
        self.__username = username




































# Schreibe eine Klasse AdminAccount, die von Account erbt.
# Überlege dir, wie man den AdminAccount besonders gegen die 
# Manipulierung von Daten schützen sollte!
# Es darf nur ein AdminAccount erstellt werden.
# Überlege dir, wie man die Erstellung eines weiteren AdminAccounts verhindern
# könnte - Exception?

# Schreibe eine Klasse PasswordManager mit zwei Attributen:
# adminAccount - vom Typ AdminAccount
# accounts - eine Liste mit Accounts
# und 4 Methoden:
# isPasswortValid(passwort) - gibt True oder False zurück
# addAccount(account) - selbsterklärend
# getAllAccounts() - gibt eine Liste aller Accounts zurück
# getAccount4Program(program) - gibt eine Liste aller Accounts zu einem bestimmten
# Programm zurück
