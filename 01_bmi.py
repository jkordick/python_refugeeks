# BMI = Körpergewicht : (Körpergröße)²

#BMI < 18,5	Untergewicht
#BMI 18,5 – 24,9 Normalgewicht
#BMI 25 – 29,9	Übergewicht
"""""
gewicht = float(input('Bitte geben Sie ihr Gewicht ein: '))

groesse = float(input('Bitte geben Sie ihre Größe in m ein: ')) # 1.76

bmi = gewicht / (groesse * groesse)

# round(number, n)
bmi = round(bmi, 2)

if bmi <= 18.4:
    print('Untergewicht')
elif 18.4 < bmi < 25:
    print('Normalgewicht')
elif 25 <= bmi <= 29.9:
    print('Übergewicht') 
else:
    print('Du bist krank')

print('Ihr BMI ist: '  + str(bmi))

"""
# Schreibe ein Programm mit einer Funktion, die zwei Übergabeparameter akzeptiert.
# groesse als float
# gewicht als float
# Die Funktion soll den BMI berechnen und ausgeben, ob die Person Untergewicht, Normalgewicht
# oder Übergewicht hat.



def bmiBerechnen1(groesse, gewicht):
    bmi = gewicht / (groesse * groesse)
    # round(number, n)
    bmi = round(bmi, 2)
    if bmi <= 18.4:
        return 'Untergewicht' 
    elif 18.4 < bmi < 25:
        return 'Normalgewicht'
    elif 25 <= bmi <= 29.9:
        return 'Übergewicht'
    else:
        return 'Du bist krank'


def bmiBerechnen2(groesse, gewicht):
    bmi = gewicht / (groesse * groesse)
    # round(number, n)
    bmi = round(bmi, 2)
    result = ''
    if bmi <= 18.4:
        result = 'Untergewicht' 
    elif 18.4 < bmi < 25:
        result = 'Normalgewicht'
    elif 25 <= bmi <= 29.9:
        result = 'Übergewicht'
    else:
        result = 'Du bist krank'
    return result

print(bmiBerechnen1(1.76, 80))
print(bmiBerechnen2(1.80, 100))    


#groesse = float(input('Größe eingeben'))
#gewicht = float(input('Gewicht eingeben'))
#print(bmiBerechnen(groesse, gewicht))

print(bmiBerechnen(1.80, 70))
print(bmiBerechnen(1.90, 120))

