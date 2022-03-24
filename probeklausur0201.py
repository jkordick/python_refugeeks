# 1) Erkläre in eigenen Worten die folgenden Begriffe:
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
# (keine Get- und Set-Methoden)

from concurrent.futures import process


class Mensch:
    def __init__(self, geschlecht, alter, groesse, gewicht):
        self.geschlecht = geschlecht
        self.alter = alter
        self.groesse = groesse
        self.gewicht = gewicht

    def __str__(self):
        return str(self.geschlecht) + ', ' + str(self.alter) + ', ' + str(self.groesse) + ', ' + str(self.gewicht)

# 3) Der folgende Programm-Abschnitt verursacht einen Fehler. 
# Wieso tritt dieser Fehler auf und was musst du tun, um diesen
# Fehler zu beheben?

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
# zusätzlich geforderten fachlichen Methoden - keine Get- und Set-Methoden.

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

class Obst:
    def __init__(self, ursprungsland, preis, name):
        self.ursprungsland = ursprungsland
        self.preis = preis
        self.name = name
    
    def __str__(self):
        return str(self.ursprungsland) + str(self.preis) + str(self.name)
    
    def aenderePreis(self, preis):
        self.preis = preis
    
    def berechneVerkaufspreis(self, gewichtInGramm): # Funktions-/Methodenkopf
        preisProGramm = self.preis/1000 
        verkaufspreis = preisProGramm * gewichtInGramm
        return verkaufspreis


class Apfel(Obst):
    def __init__(self, ursprungsland, preis, name, farbe): # def __init__(self, preis, farbe):
        super().__init__("Deutschland", preis, "Apfel")
        self.farbe = farbe
    
    def __str__(self):
        return Obst.__str__(self) + str(self.farbe)


class Banane(Obst):
    def __init__(self, ursprungsland, preis, name, reifegrad): # def __init__(self, preis, reifegrad):
        super().__init__("Brasilien", preis, "Banane")
        self.reifegrad = reifegrad

    def __str__(self):
        return Obst.__str__(self) + str(self.reifegrad)

    def berechneVerkaufspreis(self, gewichtInGramm):
        gewichtDer10Prozent = gewichtInGramm/100 * 10
        endGewicht = gewichtInGramm - gewichtDer10Prozent
        preisProGramm = self.preis/1000 
        verkaufspreis = preisProGramm * endGewicht
        return verkaufspreis


  






