# Schreibe ein Programm, mit einer Funktion, die drei Übergabeparameter akzeptiert.
# Die Übergabeparameter sind:
# Wort
# Buchstabe, der ersetzt werden soll  Bsp.: a
# Zeichen, mit dem der Buchstabe ersetzt werden soll Bsp.: *
# Die Funktion soll das neue Wort mit den ersetzten Buchstaben zurück geben.

# uebergabe

# camelCase
# snake_case
# kebap-case

def buchstabenErsetzen(wort, buchstabe, zeichen):
    neues_wort = ''
    for w in wort:
        if w == buchstabe:
            neues_wort += zeichen  
        else:
            neues_wort += w  

    return neues_wort

print(buchstabenErsetzen("intoCode", "o", "#"))

print(buchstabenErsetzen("Banane", "a", "*"))
print(buchstabenErsetzen("Schokolade", "o", "#"))
print(buchstabenErsetzen("Apfelkuchen", "e", "!"))



# Schreibe ein Programm, das einen beliebigen String einliest.
# In diesem String sollen alle 'a' durch ein '*' ersetzt werden.
# Beispiel: 
# Wort: Banane
# Ausgabe: B*n*ne

# neues_wort = input("Bitte gib ein Wort ein: ")

"""
x = ''
for w in neues_wort:
    if w == 'a':
        x += '*' # x = x + '*' 
    else:
        x = x + w # x += w
print(x)    
"""

def buchstabenErsetzen(wort, buchstabe, zeichen):
    neues_wort = ''
    i = 0
    while i < len(wort):
        if wort[i] == buchstabe:
            neues_wort += zeichen
        else:
            neues_wort += wort[i]
        i += 1
    return neues_wort

print(buchstabenErsetzen('Python', 'h', '4'))



#print(neues_wort.replace('a', '*'))