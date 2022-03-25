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

#maximalLiterTank = int(input("Bitte die maximalen Liter des Tank angeben: "))
#euroProLiter = 1.5
#tanken = int(input("Ich tanke so viele Liter: "))



#print(f"Der Betrag, den ich bezahlen muss: {summe}")
#print("Der Betrag, den ich bezahlen muss.", summe)
#print("Der Betrag, den ich bezahlen muss:"  + str(summe))



# Schreibe ein Programm mit einer Funktion, die zwei Übergabeparameter akzeptiert.
# 1. Euro pro Liter als float Bsp.: 2.10 Euro
# 2. Anzahl der Liter, die ihr tankt Bsp.: 50 Liter
# In der Funktion muss eine Variable festlegen, wie viele Liter das Auto maximal tanken kann. Bsp.: 100 Liter
# Die Funktion soll zurückgeben, wie voll der Tank ist Bsp. "Reserve" und zu wie viel Prozent der Tank gefüllt ist Bsp. 20%
# Beide Ausgaben dürfen in einem String stehen.
# Schreibe eine if-Bedingung, die bestimmt, ob das Auto auf Reserve läuft, oder nicht.

def tanken(euroProLiter, liter):
    maximalLiterTank = 80
    gefuelltInProzent = maximalLiterTank/100 * liter
    summe = euroProLiter * liter

    result = ''
    if gefuelltInProzent <= 10:
        result = 'Reserve, bitte tanken ' 
    elif 10 < gefuelltInProzent <= 100:
        result = 'Alles okay '
    elif gefuelltInProzent > 100:
        result = 'Ab in die Werkstatt '
    else:
        result = 'Irgendwas ist schief gelaufen '

    return result + str(gefuelltInProzent) + '% ' + str(summe) + '€' # Alles okay 40.0% 105.0€

print(tanken(2.10, 50))

