# Übungen  zu for - Schleifen

# Schreibe ein Programm, das eine beliebige ganze natürliche Zahl n einliest und dann n Zeilen von Sternchen
# ausgibt. 
# In der ersten Zeile 1 Sternchen, dann 2 Sternchen, dann 3, usw.
# Für n = 4 also:
# *
# **
# ***
# ****
"""""
n = int(input('Bitte gib eine Zahl ein: '))

for i in range(n + 1):
    print(i * '*')

# oder

for i in range(n):
    print((i + 1) * '*')


# Schreibe ein Programm, das eine beliebige natürliche Zahl m einliest und dann m Zeilen
# von Sternen in UMGEKEHRTER REIHENFOLGE ausgibt.
# Für m = 4 also:
# ****
# ***
# **
# * 

 #m = int(input('Bitte gib eine Zahl ein: '))

for i in range(m): 
    print((m - i) * '*')


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

# wort = input('Bitte gib ein Wort ein: ')

for w in wort:
    print(w)
"""

# Schreibe ein Programm, das einen beliebigen String einliest.
# In diesem String sollen alle 'a' durch ein '*' ersetzt werden.
# Beispiel: 
# Wort: Banane
# Ausgabe: B*n*ne

neues_wort = input("Bitte gib ein Wort ein: ")

"""
x = ''
for w in neues_wort:
    if w == 'a':
        x += '*' # x = x + '*' 
    else:
        x = x + w # x += w
print(x)    
"""
i = 0

while i < len(neues_wort):
    if neues_wort[i] == 'a':
        print('*')
    else:
        print(neues_wort[i])
    i += 1



#print(neues_wort.replace('a', '*'))

""""
wort = input('Soll ich die Maschine Starten?')

boolean = False
if wort == "Ja":
    boolean = True
else:
    boolean = False

if boolean:
    print ('ich starte die maschine')
else: 
    print('ich starte maschine NICHT')

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



# Schreibe ein Programm, das ein Rechteck aus Sternen ausgibt.
# Dazu müssen die Höhe und die Breite des Rechtecks als natürliche Zahlen eingelesen werden.
# Die Ausgabe soll beispielsweise so aussehen:

# Die Höhe ist: 4
# Die Breite ist: 3
# ***
# ***
# ***
# ***

breite = int(input('Bitte gib eine Breite ein: '))
hoehe = int(input('Bitte gib eine Höhe ein: '))

#for s in range(hoehe):
#    print(breite * '*')

s = 1
while s <= hoehe:
    print(breite * '*')
    s = s + 1


i = 1

while i <= 10:
    print(i)
    i += 1

    """




