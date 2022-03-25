# Hausaufgabe (freiwillig)
# Recherche über Vererbung (Inheritance) bzw. Polymorphie (Polymorphism)

# Schreibe eine Klasse Pruefung
# Die Klasse hat 4 Attribute: fach, person, note, bestanden
# Schreibe eine Konstruktor __init__ und eine String-Methode __str__
class Pruefung:
    def __init__(self, fach, person, note):
        self.fach = fach
        self.person = person
        self.note = note
        self.bestanden = self.hatBestanden()
        
    def __str__(self):
        return str(self.fach) + ', ' + str(self.person) + ', ' + str(self.note) + ', ' + str(self.bestanden)

    def getFach(self):
        return self.fach

    def getPerson(self):
        return self.person

    def getNote(self):
        return self.note

    def getBestanden(self):
        return self.bestanden

    def setFach(self, fach):
        self.fach = fach

    def setPerson(self, person):
        self.person = person

    def setNote(self, note):
        self.note = note

    def setBestanden(self):
        self.bestanden = self.hatBestanden()

    def aendereNote(self, note):
        self.setNote(note)

    def hatBestanden(self):
        if self.note <= 4:
            return True
        elif self.note >= 5:
            return False
        return None


pruefung = Pruefung('Theoretische Informatik', 'Julia', 4.0)
print(pruefung)

# > 50 oder 1-4 = Bestanden
# < 50 oder > 4 = nicht Bestanden 


# Schreibe getter & setter für die Attribute


# Schreibe zwei Funktionen:
# 1. aendereNote(note) um ein Note zu ändern
# 2. hatBestanden(), die den Wert von bestanden liefert


















# Erweitere die Methode aendereNote so, dass das Prüfungsergebnis nur verändert werden kann, wenn
# die note im Bereich 1.0 - 4.0 liegt.