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
mrz = 31
apr = 30
mai = 31
jun = 30
jul = 31
aug = 31
sep = 30
okt = 31
nov = 30


vergangenenTage = 0
if monate == 1:
    vergangenenTage = tage
elif monate == 2:
    vergangenenTage = jan + tage
elif monate == 3:
    vergangenenTage = jan + feb + tage
elif monate == 4:
    vergangenenTage = jan + feb + mrz + tage
elif monate == 5:
    vergangenenTage = jan + feb + mrz + apr + tage
elif monate == 6:
    vergangenenTage = jan + feb + mrz + apr + mai + tage
elif monate == 7:
    vergangenenTage = jan + feb + mrz + apr + mai + jun + tage
elif monate == 8:
    vergangenenTage = jan + feb + mrz + apr + mai + jun + jul + tage
elif monate == 9:
    vergangenenTage = jan + feb + mrz + apr + mai + jun + jul + aug + tage
elif monate == 10:
    vergangenenTage = jan + feb + mrz + apr + mai + jun + jul + aug + sep + tage
elif monate == 11:
    vergangenenTage = jan + feb + mrz + apr + mai + jun + jul + aug + sep + okt + tage
elif monate == 12:
    vergangenenTage = jan + feb + mrz + apr + mai + jun + jul + aug + sep + okt + nov + tage

print('So viele Tage sind in diesem Jahr bereits vergangen', vergangenenTage)
