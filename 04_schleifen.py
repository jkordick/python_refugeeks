# Übungen  zu for - Schleifen

# Schreibe ein Programm, das eine beliebige ganze natürliche Zahl n einliest und dann n Zeilen von Sternchen
# ausgibt. 
# In der ersten Zeile 1 Sternchen, dann 2 Sternchen, dann 3, usw.
# Für n = 4 also:
# *
# **
# ***
# ****

n = int(input('Bitte gib eine Zahl ein: '))

for i in range(n + 1):
    print(n * '*')

# oder

for i in range(n):
    print((n + 1) * '*')

# Schreibe ein Programm, das eine beliebige natürliche Zahl m einliest und dann m Zeilen
# von Sternen in UMGEKEHRTER REIHENFOLGE ausgibt.
# Für m = 4 also:
# ****
# ***
# **
# * 












# Schreibe ein Programm, das eine beliebige natürliche Zahle einliest. 
# Benutze eine for-Schleife, um alle ungeraden Zahlen, 
# die zwischen 1 und der eingebenen Zahl liegen, auszugeben.
# Beispiel:
# Zahl: 10
# Ausgabe: 1, 3, 5, 7, 9





