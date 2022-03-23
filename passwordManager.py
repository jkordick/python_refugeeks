# Wir schreiben einen Passwort-Manager

# Schreibe eine Klasse Account mit den drei Attributen
# program - das Programm, zu dem der Account gehört
# username - der Benutzername, der zum Zugang zu dem Programm verwendet wird
# password - das Passwort, das zum Zugang zu dem Programm verwendet wird
# und zwei Methoden/Funktionen:
# getProgramName() - die das zugehörige Program des Accounts zurück gibt
# changePassword(password) - um das gespeicherte Passwort zu ändern

# Schreibe eine Klasse AdminAccount, die von Account erbt.
# Überlege dir, wie man den AdminAccount besonders gegen die 
# Manipulierung von Daten schützen sollte!
# Es darf nur ein AdminAccount erstellt werden.
# Überlege dir, wie man die Erstellung eines weiteren AdminAccounts verhindern
# könnte - Exception?

# Schreibe eine Klasse PasswordManager mit zwei Attributen:
# adminAccount - vom Typ AdminAccount
# accounts - eine Liste mit Accounts
# und x Methoden:
# isPasswortValid(passwort) - gibt True oder False zurück
# addAccount(account) - selbsterklärend
# getAllAccounts() - gibt eine Liste aller Accounts zurück
# getAccount4Program(program) - gibt eine Liste aller Accounts zu einem bestimmten
# Programm zurück
