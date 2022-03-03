# Übung zu for - Schleifen
# Schreibe ein Programm, das eine beliebige ganze natürliche Zahl n einliest und dann n Zeilen von Sternchen
# ausgibt. 
# In der ersten Zeile 1 Sternchen, dann 2 Sternchen, dann 3, usw.
# Für n = 4 also:
# *
# **
# ***
# ****

n = int(input('Bitte gib eine Zahl ein: '))

for i in range(n+1):
    print(n * '*')

# oder

for i in range(n):
    print((n+1)* '*')