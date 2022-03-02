# Schreiben Sie ein Programm, dass für ein eingegebenes beliebiges 
# Datum die Anzahl der bisher im Jahr
# vergangenen Tage ausgibt. 
# (Der Einfachheit halber soll davon ausgegeben werden, dass der Februar
# immer 28 Tage hat.)

# Beispiel:
# Eingabe Tag: 12
# Eingabe Monat: 7
# Ausgabe Tage seit Jahresanfang: 193

# Bei fehlerhaften Eingaben, wie dem 31.02. sollen Fehler ausgegeben werden

# Wie viele Tage hat jeder Monat?
# Das gesamte Jahr hat 365 Tage
# 31 Tage: Januar, März, Mai, Juli, August, Oktober, Dezember
# 30 Tage: April, Juni, September, November
# 28 Tage: Februar

tage = int(input('Tage: '))
monate = int(input('Monat: '))

jan = 31
feb = 28

vergangenenTage = 0
if monate == 1:
    vergangenenTage = tage
elif monate == 2:
    vergangenenTage = jan + tage

print('So viele Tage sind in diesem Jahr bereits vergangen', vergangenenTage)
