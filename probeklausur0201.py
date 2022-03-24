# 1) Erkläre in eigenen Worten die folgenden Begriffe: # 6
# * Konstruktor # spezielle Methode/Funktion - initialisiert das Objekt, das aus der Klasse erstellt wird 
# - ist notwendig, um ein ein Objekt aus einer Klasse erstellen zu können - instanziiert ein Objekt aus der Klasse
# * Vererbung # wichtiges Konzept der objektorientierten Softwareentwicklung - 
# Eltern & Kindklasse oder Super & Subklasse - die Kindklassen alle Attribute und Methoden/Funktionen
# der Elternklasse erben
# * Dictionary (Datenstruktur) - werden Datensätze nach dem Key/Value bzw Schlüssel/Wert-Prinzip gespeichert
# - ist veränderbar - erlaubt keine Duplikate in den Keys bzw. Schlüsseln

# 2) Schreibe eine Klasse Mensch mit den vier Attributen
# geschlecht, alter, groesse und gewicht
# Schreibe einen Konstuktor und eine String-Methode
# (keine Get- und Set-Methoden) # 5

class Mensch: # 1
    def __init__(self, geschlecht, alter, groesse, gewicht): #1
        self.geschlecht = geschlecht #1
        self.alter = alter
        self.groesse = groesse
        self.gewicht = gewicht

    def __str__(self): #1
        return str(self.geschlecht) + ', ' + str(self.alter) + ', ' + str(self.groesse) + ', ' + str(self.gewicht) #1

# 3) Der folgende Programm-Abschnitt verursacht einen Fehler. 
# Wieso tritt dieser Fehler auf und was musst du tun, um diesen
# Fehler zu beheben? # 4

class Milkshake:
    def __init__(self, groesse, geschmack):
        self.groesse = groesse
        self.geschmack = geschmack

    def __str__():
        return str(self.groesse) + ', ' + str(self.geschmack)

# Der Fehler tritt auf, da wir versuchen (Klassen-)Attribute in der String-Methode aufzurufen, aber wir
# haben der Methode String keinen Parameter self übergeben.
# Um den Fehler zu beheben müssen wir der String-Methode den Übergabeparameter self geben.

# Mit self werden Klassen-Attribute und Methoden gekennzeichnet.

# 4) Schreibe alle Datentypen und Datenstrukturen auf, die wir bisher
# in Python kennengelernt haben.
# integer, string, float, boolean, none, list, tuple, dictionary

# 5) Schreibe ein Programm. Schreibe nur Konstuktoren und die String-Methoden und 
# zusätzlich geforderten fachlichen Methoden - keine Get- und Set-Methoden. #27

# Schreibe eine Klasse Obst mit drei Attributen:
# * urspungsland - das Land, in dem das Obst angebaut und geerntet wurde
# Bsp.: Deutschland
# * preis - der Preis für das Obst pro kg - Bsp.: 1 Euro
# * name - der Name des Obst
# Schreibe zwei fachliche Methoden:
# * änderePreis(preis) - um den Preis zu dem das Obst pro kg verkauft wird zu ändern
# * berechneVerkaufspreis(gewicht) - um den Verkaufspreis des Obst anhand des Gewichts zu
# berechnen

# Schreibe zwei Kinderklassen Banane und Apfel. Beide Klassen sollen
# für die geerbten Attribute urspungsland und name einen festen Wert festlegen.

# Die Klasse Apfel bekommt ein zusätzliches Attribut:
# * farbe - das an gibt, welche Farbe der Apfel hat - Bsp.: rot
# Die Klasse Banane bekommt ein zusätzliches Attribut:
# * reifegrad - das an gibt, wie reif die Banane ist Bsp.: weich
# Überschreibe in der Klasse Banane die Methode 
# berechneVerkaufspreis, indem wir davon ausgehen, dass von
# Bananen immer 10% Gewicht abgezogen werden, aufgrund der Schale

class Obst: #1
    def __init__(self, ursprungsland, preis, name): #1
        self.ursprungsland = ursprungsland #1
        self.preis = preis
        self.name = name
    
    def __str__(self): #1
        return str(self.ursprungsland) + str(self.preis) + str(self.name) #1
    
    def aenderePreis(self, preis): #1
        self.preis = preis #1
    
    def berechneVerkaufspreis(self, gewichtInGramm): # Funktions-/Methodenkopf #1
        preisProGramm = self.preis/1000 
        verkaufspreis = preisProGramm * gewichtInGramm
        return verkaufspreis #1

# 9


class Apfel(Obst): #2
    def __init__(self, ursprungsland, preis, name, farbe): # def __init__(self, preis, farbe): #1
        super().__init__("Deutschland", preis, "Apfel") #2
        self.farbe = farbe #1
    
    def __str__(self): #1
        return Obst.__str__(self) + str(self.farbe) #1

# 8


class Banane(Obst): #2
    def __init__(self, ursprungsland, preis, name, reifegrad): # def __init__(self, preis, reifegrad): #1
        super().__init__("Brasilien", preis, "Banane") #2
        self.reifegrad = reifegrad #1

    def __str__(self): #1
        return Obst.__str__(self) + str(self.reifegrad) #1

    def berechneVerkaufspreis(self, gewichtInGramm): #1
        gewichtDer10Prozent = gewichtInGramm/100 * 10
        endGewicht = gewichtInGramm - gewichtDer10Prozent
        preisProGramm = self.preis/1000 
        verkaufspreis = preisProGramm * endGewicht
        return verkaufspreis #1

# 10


# 42


  






