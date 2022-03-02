# 1
# eingabe liter die der tank eures autos maximal fasst
# eingabe/festlegen kosten euro/liter 
# eingabe wieviel ihr tankt in liter
# ausgabe der summe der getankten liter

# 2
# ausgabe zu wie viel % der tank gefüllt ist
# wenn der tank unter 10% gefüllt ist: ausgabe "Reserve, bitte tanken"
# wenn der tank zwischen 11% und 100% gefüllt ist: ausgabe "Alles OK"
# wenn der tank zu mehr als 100% gefüllt ist: ausgabe "Ab in die Werkstatt"

maximalLiterTank = int(input("Bitte die maximalen Liter des Tank angeben: "))
euroProLiter = 1.5
tanken = int(input("Ich tanke so viele Liter: "))

summe = euroProLiter * tanken

print(f"Der Betrag, den ich bezahlen muss: {summe}")
print("Der Betrag, den ich bezahlen muss.", summe)
print("Der Betrag, den ich bezahlen muss:"  + str(summe))



gefuellt = maximalLiterTank/100 * tanken

if gefuellt <= 10:
    print('Reserve, bitte tanken')
elif 10 < gefuellt <= 100:
    print('Alles okay')
elif gefuellt > 100:
    print('Ab in die Werkstatt')
else:
    print('Irgendwas ist schief gelaufen')

