# 1. Aufgabe
# wenn die Note einer Schülerin kleiner oder gleich 4.0 ist
# dann print Bestanden
# sonst print Nicht Bestanden

def noteAuswerten(note):
    if note <= 4.0:
        print("Bestanden")
    else:
        print("Nicht Bestanden")

noteAuswerten(3.0)

# 2. Aufgabe
# setze einen Zähler auf 0
# erstelle eine leere Liste Namen
# so lange der Zähler kleiner oder gleich 10 ist
#   input Name
#   Name zur Liste Namen hinzufügen
#   Zähler + 1
# print Namen
"""
def namenListeErstellen(zaehler):
    namen = []
    while zaehler <= 10:
        name = input("Bitte gib einen Namen ein")
        namen.append(name)
        zaehler += 1 # zaehler = zaehler + 1
    print(namen)

namenListeErstellen(0)

"""
# 3. Aufgabe
# namenHinzufuegen(liste)
#   setze einen Zähler auf 0 # falle
#   so lange Zähler <= 10
#       input Name
#       Name zur Liste hinzufügen            
#       Zähler + 1
#       namenHinzufuegen(liste)

# zähler benutzen den als abbruchbedingung
# oder benutzen die länge der liste als abbruchbedingung

# Aufruf von namenHinzufügen mit einer leeren Liste

def namenHinzufügen(liste):
    if len(liste) > 3: # Abbruchbedingung
        print(liste)
        return
    else: 
        name = input("Bitte gib einen Namen ein: ")
        liste.append(name)
        namenHinzufügen(liste)
namenHinzufügen([])


def namenHinzufügen2(liste, zaehler):
        if zaehler > 3: # Abbruchbedingung
            print(liste)
            return
        else:
            name = input("Bitte gib einen Namen ein")
            liste.append(name)
            namenHinzufügen2(liste, zaehler + 1)
namenHinzufügen2([], 0)
