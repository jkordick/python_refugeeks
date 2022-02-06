# for schleife
names = ["Joe", "Max", "Kelvin"]

# Anweisung für alle Strings anwenden
for x in names:
    print(x)

# Schleife bei Bedingung abbrechen
for x in names:
    print(x)
    if x == "Max":
        break

# Anweisung 10-mal ausführen
for x in range(10):
    print(x)

# while-schleife
i = 1
while i < 6:
    print(i)
    i += 1

# auch while-schleife kann abgebrochen werden
i = 1
while i < 10:
    print(i)
    if i == 3:
        break
    i += 1
