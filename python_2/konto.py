# This Python file uses the following encoding: utf-8
# Teil 1
# Schreibe eine Klasse Konto mit einen Kontoinhaber, einer Kontonummer und einem Kontostand
# Der Name des Kontoinhabers soll geaendert werden können, die Kontonummer aber nicht.
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

# Schreibe eine eigene Exception, die in dem Fall, dass auf dem Konto nicht genug Guthaben vorhanden ist
# geworfen wird und ausgibt: "Weil der Kontostand zu gering ist, kann keine Auszahlung gemacht werden."
# Fange deine Exception in einem try/except

# Schreibe eine eigene Exception, die in dem Fall, dass der Dispokredit überzogen wird geworfen wird und ausgibt:
# "Sie haben ihren Dispokredit ausgeschöpft."
# Fange deine Exception in einem try/except

class GuthabenException(Exception):
    def __str__(self):
        return "Weil der Kontostand zu gering ist, kann keine Auszahlung gemacht werden."

class DispoException(Exception):
    def __str__(self):
        return "Sie haben ihren Dispokredit ausgeschöpft."

class Konto: 
    def __init__(self, kontoinhaber, kontonummer, kontostand):
        self.kontoinhaber = kontoinhaber
        self.__kontonummer = kontonummer
        self.kontostand = kontostand
    

    def __str__(self):
        return str(self.kontostand) + ', ' + str(self.__kontonummer) + ', ' + str(self.kontostand)
    
    
    def setKontoinhaber(self, neuer_kontoinhaber):
        self.kontoinhaber = neuer_kontoinhaber
    
    # kontonummer private ODER bieten keinen Setter an ODER wir schreiben einen Dummy-Setter
    def setKontonummer(self, neue_kontonummer):
        return
    
    def getKontonummer(self):
        return self.__kontonummer
    
    def einzahlen(self, betrag):
        self.kontostand += betrag
    
    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag
        else: 
            raise GuthabenException()

# Kinderklassen bzw Subklassen erben von den Elternklassen Attribute UND Methoden/Funktionen
class Festgeldkonto(Konto):
     def __init__(self, kontoinhaber, kontonummer, kontostand):
         Konto.__init__(self, kontoinhaber, kontonummer, kontostand)
         self.zinssatz = 5
    
     def __str__(self):
        return Konto.__str__(self) + ', ' + str(self.zinssatz)

    # Aufgabe der Bank?
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
            raise DispoException()

# super().Methode(): über die Methode super() rufen wir die Methode der Superklasse auf 
# Superklasse.Methode(self): über den Namen der Superklasse rufen wir die Methode der Superklasse auf und müssen
# dann den Übergabeparameter self verwenden

# Teil 2 Hausaufgabe (freiwillig)
# 1. Finde heraus, wie man in Python Attribute und Methoden als privat markieren kann. 
# Dabei gibt es bei Python einige Besonderheiten.
# Setze die Kontonummer in der Klasse Konto auf privat.

# 2. Erweitere unser heutiges Programm um eine Klasse Bank. Überlege dir, wie eine Bank verschiedene
# Konten verwalten könnte und welche Attribute und Methoden Teil der Klasse Bank sein sollten.

konto = Konto('Sofiane', 12345, 200.00)
girokonto = Girokonto('Viktoria', 1121212, 2000.00, 0)

try:
    konto.abheben(300.00)
except:
    print(GuthabenException())

try: # ausprobieren, ob das Programm läuft # brauchen wir IMMER
    girokonto.abheben(3000.00)
except: # wenn ein Fehler auftritt # oder finally # wenn finally vorhanden, dann auch optional
    print(DispoException())
else: # wenn kein Fehler auftritt # optional
    print('Alles in Ordnung')
finally: # wird immer ausgeführt # oder except # wenn except vorhanden, dann auch optional
    print('Finally')

    
