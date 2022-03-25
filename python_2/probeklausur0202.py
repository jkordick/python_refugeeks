# 1) 6 Punkte
# Klasse - Basis/Konzept der Objektorientierung, (Attribute, Methoden) 
# Konstruktor, String-Methode, get- und set-Methoden, Basis zur (Instanziierung von Objekten bzw zur Erstellung von Objekten)
# Verwaltung von Daten
# Objekt - (Instanziierung einer Klasse, einfacher: Werden aus Klassen erstellt ODER werden von Klassen definiert)
# zur Verwaltung von komplexen/komplizierteren Datenstrukturen
# Exception - (Klassen, die helfen, Fehler im Programm zu behandeln) # es können eigene Exceptions definiert werden
# werden mit raise, try und except behandelt # vermeiden, dass das Programm im Falle eines Fehlers abbricht

# 2) 4 Punkte
class DispokreditException(Exception): #2
    def __str__(self): #1
        return "Sie haben ihren Dispokredit ausgeschöpft" #1

# 3) 4 Punkte
class Ball:
    def __init__(self, sport, groesse):
        self.sport = sport
        self.groesse = groesse
    
    def __str__(self):
        return ""

    def setSport(self, sport):
        self.sport = sport

# Weil self nicht als Übergabeparameter in setSport mitgegeben wurde,  # 1  
# kann nicht auf das Attribut self.sport zugegriffen werden. # 2
# Es muss der Übergabeparameter self zusätzlich zu sport in der Methode setSport übergeben werden. # 1 

# 4) 4 Punkte
# get-Methoden: (Lesenden-)Zugriff auf Attribute der Klasse #1 und geben die Werte der Attribute zurück #1
# set-Methoden: (Schreibend-)Zugriff auf Attribute der Klasse #1, verändert ein Attribut der Klasse
# oder setzt den Wert eines Attributs der Klasse #1

# 5)

class Tier: #1
    def __init__(self, saeugetier, name, lebtImMeer): #1
        self.saeugetier = saeugetier #1
        self.name = name
        self.lebtImMeer = lebtImMeer

    def __str__(self): #1
        return str(self.saeugetier) + str(self.name) + str(self.lebtImMeer) #1
    
    def istMeeressaeugetier(self): #1
        return self.saeugetier and self.lebtImMeer #1
    
    def getTiername(self): #1
        return self.name #1

# 9

class Delphin(Tier): #2
    def __init__(self, saeugetier, name, lebtImMeer, isstFisch): #1 # def __init__(self, saeugetier, name, lebtImMeer):
        super().__init__(saeugetier, name, lebtImMeer) #1 Tier.__init__(self, saeugetier, name, lebtImMeer)
        self.isstFisch = True #1

    def __str__(self): #1
        return super().__str__() + str(self.isstFisch) #2

# 8

class Clownfisch(Tier): #2
    def __init__(self, saeugetier, name, lebtImMeer): #1
        super().__init__(saeugetier, name, lebtImMeer) #1 # ruft den Konstruktor der Super-Klasse bzw Eltern-Klasse
    
    def __str__(self): #1
        return super().__str__() #1
    
    def getErnaehrung(self): #1
        return "Plankton und Algen" #1

# 8

# 25 
    


    
    

    
