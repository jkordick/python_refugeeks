""""
# Aufgabe 1

# Programmiersprache: Sprache, in der wir ein Programm schreiben, 
                    # Sprache, in der wir Anweisungen schreiben, 
                    # Sprache, mit der Algorithmen (be-)schreiben werden
                    # Bonus: um Probleme zu lösen
                    # Bonus 2: Python, Java, C#, Javascript, C, C++, PHP
# Algorithmus: werden in Programmiersprachen geschrieben/formuliert, sind oder haben Anweisungen, die abgearbeitet werden
                # Teil eines Programms
                # Bonus: um Probleme zu lösen
                # Bonus 2: Kochrezept, Möbelaufbauanleitung, ...
# Programm: wird ausgeführt, um Probleme zu lösen, enthält einen Algorithmus, enthält Algorithmen
        # wird in einer Programmiersprache geschrieben oder beschrieben oder formuliert
        # Bonus: wird auf dem PC ausgeführt
        # Bonus 2: wird kompiliert oder interpretiert
            

# Aufgabe 2

celsius = int(input('Gib die Grad in Celsius an: '))
fahrenheit = (celsius * (9/5)) + 32
print(str(fahrenheit))


# Aufgabe 3

tipp = int(input('Errate eine Zahl: '))
if tipp == 3:
    print('Gewonnen')
else: 
    print('Verloren')
print('Das Spiel ist aus')



# Aufgabe 4

print(5/2) # 2.5
print(12/2*2) # 12.0
print(12/2**2) # 3.0
print(5//2) # 2
print(5%2) # 1
print(7/2 > 1+3) # False
print(1+1) # 2
print(1+1.0) # 2.0
# print(1+'1') # Fehler
print('1'+'1') # '11'
print(not True and False) # False
print(True or False and False) # True () > not > and > or
print((True or False) and False) # False



# Aufgabe 5
def berecheneKreis(radius):
    flaeche = 3.14 * (radius * radius)
    # flaeche = 3.14 * (radius ** 2)
    return flaeche

print(berecheneKreis(5))

def berechneQuadrat(laenge):
    flaeche = laenge ** 2
    # flaeche = laenge * laenge
    print(str(flaeche))


def berechneRechteck(laenge, breite):
    flaeche = laenge * breite
    print(str(flaeche))

berechneRechteck(5, 7)

"""""


# Aufgabe 6
def buchstabenErsetzen(wort, buchstabe, zeichen): # Definition, Funktion, Übergabeparameter
    neues_wort = '' # neue Variable anlegen oder Deklaration einer Variable oder Initialisierung einer Variable, (leerer) String
    for w in wort: # for-Schleife, Laufvariable, iterieren oder Beginn bis zum Ende des Wortes 'durcharbeiten' oder 
                # Betrachtung jedes Buchstabens des Wortes oder wort ist ein String und ein String ist eine Liste von Buchstaben
        if w == buchstabe: # if-Bedingung, Vergleich oder vergleichen, wir vergleichen die Laufvariable w mit dem Übergabeparameter buchstabe
            neues_wort += zeichen # wenn if wahr oder true ist, dann speichern wir in der Variable neues_wort den Übergabeparameter zeichen
        else:   # wenn if falsch oder false ist, dann betrachten wir else oder führen den else-Zweig aus
            neues_wort += w # wenn if falsch oder false ist, dann speichern in der Variable neues_wort die Laufvariable w
    return neues_wort # wenn die Schleife zu ende ist oder durchgelaufen ist, dann geben wir die Variable neues_wort zurück

print(buchstabenErsetzen("intoCode", "o", "#"))

