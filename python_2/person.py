class Person:
    # Schreibe eine Klasse Person.
    # Die Klasse Person hat vier Attribute: name, gewicht, groesse, alter
    # Schreibe einen Konstruktor __init__ und eine String-Methode __str__
    # Schreibe für alle vier Attribute je eine get-Methode und eine set-Methode, also insgesamt 8 Methoden

    def __init__(self, name, gewicht, groesse, alter, wohnort):
        self.name = name
        self.gewicht = gewicht
        self.groesse = groesse 
        self.alter = alter
        self.wohnort = wohnort
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.gewicht) + ' ' + str(self.groesse) + ' ' + str(self.alter) + ' ' + str(self.wohnort)

    # camelCase getName
    # snake_case get_name
    # kebab-case get-name

    def getWohnort(self):
        return self.wohnort

    def getName(self):
        return self.name
    
    def getGewicht(self):
        return self.gewicht

    def getGroesse(self):
        return self.groesse
    
    def getAlter(self):
        return self.alter
    
    def setWohnort(self, neuer_wohnort):
        self.wohnort = neuer_wohnort
    
    def setName(self, neuer_name):
        self.name = neuer_name

    def setGewicht(self, neues_gewicht):
        self.gewicht = neues_gewicht

    def setGroesse(self, neue_groesse):
        self.groesse = neue_groesse

    def setAlter(self, neues_alter):
        self.alter = neues_alter
    

    # Schreibe zwei Funktionen: nehmeZu(kg) und nehmeAb(kg), um gewicht verändern zu können
    # nehmeZu(10): return gewicht + 10; nehmeAb(10): return gewicht - 10

    def nehmeZu(self, kg):
        return self.gewicht + kg

    def nehmeAb(self, kg):
        self.gewicht -= kg
        return self.gewicht
    
    # Für die Schnellen: 
    # Schreibe eine Methode getBMI(), die den BMI der Person zurück gibt

    def getBMI(self):
        return self.gewicht / (self.groesse ** 2)

    # Hausaufgabe (freiwillig)

    # Füge ein weiteres Attribut wohnort hinzu, schreibe eine get-Methode und eine
    # set-Methode für Wohnort

    # Schreibe die Klasse Person fertig.
    # Erstelle eine neue Datei und erzeuge in ihr
    # neue Objekte vom Typ Person und teste die 
    # implementierten Funktionen.
    # Tipp: Dazu musst du die Klasse Person in der neuen Datei
    # importieren.  

 






























