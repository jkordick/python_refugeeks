# Hausaufgabe (freiwillig)
# 1. Welche anderen Beziehungen zwischen Klassen, außer Vererbung gibt es?

# Finde heraus, wie man die Klasse Person, die wir bereits geschrieben haben 
# als Typ der Variable Besitzer unserer Klasse Haustier verwenden kann.
# Beispiel: besitzer = Person('Julia', 31)

# 2. Finde heraus, wie so genannte Mehrfachvererbung funktioniert und mache unsere Klasse
# Schlange zu einer Kind-Klasse von Haustier UND Wildtier.
# Beispiel: schlange = Schlange(fell, gewicht, groesse, besitzer, kontinent)
# print(schlange) # False, 2, 2.00, 'Julia', 'Australien'

from datei import Person

class Tier: # Superklasse / Elternklasse
    def __init__(self, fell, gewicht, groesse): # fell boolean(True or False)
        self.fell = self.setFell(fell)
        self.gewicht = gewicht
        self.groesse = groesse
    
    def __str__(self):
        return 'Fell: ' + str(self.fell) + ', Gewicht: ' + str(self.gewicht) + ', Größe: ' + str(self.groesse)
    
    def setFell(self, fell):
        if fell is True or fell is False:
            self.fell = fell
            return self.fell
        return None

class Haustier(Tier):
    def __init__(self, fell, gewicht, groesse, name_person, gewicht_person, groesse_person, alter_person, wohnort_person):
        super().__init__(fell, gewicht, groesse)
        self.besitzer = Person(name_person, gewicht_person, groesse_person, alter_person, wohnort_person)
    
    def __str__(self):
        return super().__str__() + ' ' + str(self.besitzer)

class Wildtier(Tier):
    def __init__(self, fell, gewicht, groesse, kontinent):
        super().__init__(fell, gewicht, groesse)
        self.kontinent = kontinent
    
    def __str__(self):
        return super().__str__() + ' ' + str(self.kontinent)

class Elephant(Wildtier):
    def __init__(self, fell, gewicht, groesse, ruessellänge, kontinent):
        super().__init__(fell, gewicht, groesse, kontinent)
        self.ruessellänge = ruessellänge
    
    def __str__(self):
        return 'Elephant: ' + super().__str__() + ', Rüssellänge: ' + str(self.ruessellänge)
    

class Pinguin(Wildtier): 
    def __init__(self, fell, gewicht, groesse, laeuft_suess, kontinent):
        super().__init__(fell, gewicht, groesse, kontinent)
        self.laeuft_suess = laeuft_suess
    
    def __str__(self):
        return 'Pinguin: ' + super().__str__() + ', Läuft süß: ' + str(self.laeuft_suess)
    

class Katze(Haustier):
    def __init__(self, fell, gewicht, groesse, schnurrhaare, besitzer):
        super().__init__(fell, gewicht, groesse, besitzer)
        self.schnurrhaare = schnurrhaare
    
    def __str__(self):
        return 'Katze: ' + super().__str__() + ', Schnurrhaare: ' + str(self.schnurrhaare)
    
class Schlange(Haustier, Wildtier):
    def __init__(self, fell, gewicht, groesse, keineBeine, besitzer, kontinent):
        Haustier.__init__(self, fell, gewicht, groesse, besitzer) # super-Konstruktor von Haustier
        Wildtier.__init__(self, fell, gewicht, groesse, kontinent) # super-Kontstruktor von Wildtier
        # super().__init__() == Superklasse.__init__(self)
        self.keineBeine = keineBeine
    
    def __str__(self):
        return 'Schlange: ' + super().__str__() + ', Keine Beine: ' + str(self.keineBeine)
       
class Hund(Haustier):
    def __init__(self, fell, gewicht, groesse, besteFreunddesMenschen, besitzer):
        super().__init__(fell, gewicht, groesse, besitzer)
        self.besteFreunddesMenschen = besteFreunddesMenschen
    
    def __str__(self):
        return 'Hund: ' + super().__str__() + ', Bester Freund des Menschen: ' + str(self.besteFreunddesMenschen)
       
class Goldfisch(Haustier):
    def __init__(self, fell, gewicht, groesse, kannUnterWasserAtmen, besitzer):
        super().__init__(fell, gewicht, groesse, besitzer)
        self.kannUnterWasserAtmen = kannUnterWasserAtmen
    
    def __str__(self):
        return 'Goldfisch: ' + super().__str__() + ', Kann unter Wasser atmen: ' + str(self.kannUnterWasserAtmen)
       


tier = Tier(True, 2, 2.00)
print(tier)
katze = Katze(True, 3.5, 0.15, True)
print(katze)