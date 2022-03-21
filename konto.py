# Teil 1
# Schreibe eine Klasse Konto mit einen Kontoinhaber, einer Kontonummer und einem Kontostand
# Der Name des Kontoinhabers soll geändert werden können, die Kontonummer aber nicht.
#
# Schreibe eine Sub bzw. Kinderklasse Festgeldkonto, das kann mit einem gegebenen Zinssatz 
# verzinst werden, der Zinssatz soll für alle Festgeldkonten gleich sein.
#
# Schreibe eine Sub bzw. Kinderklasse Girokonto (im Gegensatz zu allen anderen Konten) um einen bestimmten Betrag - den
# Dispokredit - überzogen werden kann.

# Für alle drei Kontoarten sollen Einzahlungen möglich sein.

# Für alle drei Kontoarten sollen Abhebungen möglich sein.
# Für ein normales Konto und ein Festgeldkonto können nur Beträge abgehoben werden, die
# kleiner als der Kontostand sind. Für ein Girokonto kann das Konto bis zu dem Betrag überzogen
# werden, der durch Dispokredit festgelegt ist.

class Konto: 
    def __init__(self, kontoinhaber, kontonummer, kontostand):
        self.kontoinhaber = kontoinhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
    
    def __str__(self):
        return str(self.kontostand) + ', ' + str(self.kontonummer) + ', ' + str(self.kontostand)
    
    def setKontoinhaber(self, neuer_kontoinhaber):
        self.kontoinhaber = neuer_kontoinhaber
    
    # kontonummer private ODER bieten keinen Setter an ODER wir schreiben einen Dummy-Setter
    def setKontonummer(self, neue_kontonummer):
        return
    
    def einzahlen(self, betrag):
        self.kontostand += betrag
    
    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag
        else: 
            print("Die Auszahlung kann nicht durchgeführt werden.")

# Kinderklassen bzw Subklassen erben von den Elternklassen Attribute UND Methoden/Funktionen
class Festgeldkonto(Konto):
     def __init__(self, kontoinhaber, kontonummer, kontostand):
         Konto.__init__(self, kontoinhaber, kontonummer, kontostand)
         self.zinssatz = 5
    
     def __str__(self):
        return Konto.__str__(self) + ', ' + str(self.zinssatz)

     def berechneZins(self):
         self.kontostand = ((self.kontostand/100) * self.zinssatz) + self.kontostand

class Girokonto(Konto):
     def __init__(self, kontoinhaber, kontonummer, kontostand, dispokredit):
         super().__init__(kontoinhaber, kontonummer, kontostand)
         self.dispokredit = dispokredit

     def __str__(self):
        return super().__str__() + ', ' + str(self.dispokredit)
    
    # überladen bzw überschreiben eine Methode/Funktion
     def abheben(self, betrag):
        if betrag <= self.kontostand + self.dispokredit:
            self.kontostand -= betrag
        else: 
            print("Die Auszahlung kann nicht durchgeführt werden.")


    
