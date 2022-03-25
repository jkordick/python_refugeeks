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