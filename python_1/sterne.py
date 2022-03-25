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




