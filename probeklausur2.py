# Aufgabe 1

# Python: Programmiersprache, coden oder programmieren, Bonus: Python wird interpretiert und nicht kompiliert
# Funktion: Übergabeparameter, mehrere Anweisungen gemeinsam, 
            # Ergebnis wird mit return oder Rückgabewert zurück gegeben, wird definiert
# Komplexität: Schwierigkeit von Problemen, verschiedene Schwierigkeitsgrade,
            # beschreibt, wie kompliziert es ist ein Problem zu lösen
            # Bonus: große Probleme in kleine Probleme teilen

# Aufgabe 2
"""
namen = ["Kelvin", "Julia", "Melanie"]

for n in namen:
    print(n, ' hat in den letzten 2 Wochen Python gelernt')

# Aufgabe 3

# String 
# integer
# float
# boolean 
# None
# liste

"""

# Aufgabe 4
# () > ** > * / // > + -
# () > not > and > or
"""
print(7 / 2)
print(6 / 3 * 2)
print(6 / 3 ** 2)
print(7 // 2)
print(7 % 2)
print(5 / 2 < 1 + 3)
print(2 + 2)
print(2 + 2.0)
# print(2 + '2')
print('2' + '2')
print(True or False)
print(False and False)
print((True or False) and True)
"""

# Aufgabe 3

"""

def berechneUmfangDreieck(kante1, kante2, kante3):
    umfang = kante1 + kante2 + kante3
    print(str(umfang))

def berechneUmfangKreis(radius):
    umfang = 2 * 3.14 * radius
    print(umfang)

def berechneUmfangRechteck(kante1, kante2):
    umfang = 2 * kante1 + 2 * kante2
    return umfang

print(berechneUmfangRechteck(2, 5))

berechneUmfangKreis(5)

"""

# Aufgabe 6

def buchstabenErsetzen(wort, buchstabe, zeichen): # Funktion, mit drei Übergabeparametern, Definition
    neues_wort = '' # neue Variable mit dem Wert eines leeren Strings, deklarieren eine Variable, initialisieren eine Variable
                    # lege eine Variable an und weise ihr den Wert eines leeren Strings zu
    i = 0   # Laufvariable, Index, neue Variable und hat den ganzzahligen/Integer Wert 0 
    while i < len(wort): # while Schleife, Laufvariable, prüfen Bedingung, Länge des Übergabeparameters, Aufruf der len-Funktion
                        # Schleife läuft so lange, bis i >= Länge des Übergabeparameters wort ist
        if wort[i] == buchstabe: # if-Bedingung, Vergleich, greifen über den Index/Laufvariable i
                                # auf ein Element im Übergabeparameter wort zu, Vergleichen diesen wert mit dem
                                # Übergabeparameter buchstabe
            neues_wort += zeichen # wenn if wahr/true wird dann speichern wir in der Variable neues_wort den 
                                    # Übergabeparameter zeichen, Konkatenation, konkatenieren
        else: # wenn if false/falsch wird, wird diese Anweisung ausgeführt
            neues_wort += wort[i] # konkatenieren, speichern in der Variable neues_wort den Wert von 
                                    # Übergabeparameter wort an Stelle des Index/der Laufvariable i
        i += 1 # Laufvariable/Index, iterieren, addition von 1
    return neues_wort # return/Rückgabewert der Variable neues_wort

print(buchstabenErsetzen('Python', 'h', '4'))
