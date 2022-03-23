# 1) Erkläre in eigenen Worten die folgenden Begriffe:
# * Konstruktor
# * Vererbung
# * Dictionary (Datenstuktur)

# 2) Schreibe eine Klasse Mensch mit den vier Attributen
# geschlecht, alter, groesse und gewicht
# Schreibe einen Konstuktor und eine String-Methode
# (keine Get- und Set-Methoden)

# 3) Der folgende Programm-Abschnitt verursacht einen Fehler. 
# Wieso tritt dieser Fehler auf und was musst du tun, um diesen
# Fehler zu beheben?

class Milkshake:
    def __init__(self, groesse, geschmack):
        self.groesse = groesse
        self.geschmack = geschmack
    
    def __str__():
        return str(self.groesse) + ', ' + str(self.geschmack)

# 4) Schreibe alle Datentypen und Datenstrukturen auf, die wir bisher
# in Python kennengelernt haben.

# 5) Schreibe ein Programm, mit dessen Hilfe du einen Einkauf im Supermarkt
# simulieren kannst. Schreibe nur Konstuktoren und die String-Methode und 
# zusätzlich geforderten fachlichen Methoden - keine Get- und Set-Methoden

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



