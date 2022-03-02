# BMI = Körpergewicht : (Körpergröße)²

#BMI < 18,5	Untergewicht
#BMI 18,5 – 24,9 Normalgewicht
#BMI 25 – 29,9	Übergewicht

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