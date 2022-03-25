# Schreibe ein Programm, das einen beliebigen String einliest und
# diesen dann buchstabenweise ausgibt.
# Beispiel:
# Wort: Banane
# B
# a
# n
# a
# n
# e

wort = input('Bitte gib ein Wort ein: ')

for w in wort:
    print(w)

# Schreibe ein Programm, das eine beliebige natürliche Zahl einliest. 
# Benutze eine for-Schleife, um alle ungeraden Zahlen, 
# die zwischen 1 und der eingebenen Zahl liegen, auszugeben.
# Beispiel:
# Zahl: 10
# Ausgabe: 1, 3, 5, 7, 9
# oder: 
# 1
# 3
# 5
# 7
# 9


zahl = int(input("Bitte gib eine Zahl ein: "))

for z in range(zahl + 1):
    if z % 2 == 1:
        print(z)
