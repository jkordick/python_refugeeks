def say_hello():
    return 'Hello'

# print(say_hello())


def addition(erster_wert, zweiter_wert):
    ergebnis = erster_wert + zweiter_wert
    return int(ergebnis)

#print(addition(7, 3))


def subtraktion(zweiter_wert):
    erster_wert_neu = addition(1, 5)  # 6
    ergebnis = erster_wert_neu - zweiter_wert
    return int(ergebnis)


print(subtraktion(2))


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
            neues_wort += zeichen  # x = x + '*'
        else:
            neues_wort += w  # x += w

    return neues_wort

print(buchstabenErsetzen("Julia", "i", "!"))

print(buchstabenErsetzen("Banane", "a", "*"))
print(buchstabenErsetzen("Schokolade", "o", "#"))
print(buchstabenErsetzen("Apfelkuchen", "e", "!"))
