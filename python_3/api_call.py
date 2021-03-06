import requests
import json
#API: application programming interface -> Anwendungsschnittstelle oder Programmierschnittstelle

#print(response.text) # String

# Internet iPhone von Julia
# PW: 11223344

# Schreibe eine Funktion, die einen request durchführt, um mehrere people zu erhalten.
# Als request könnt ihr verwenden: https://swapi.dev/api/people/
# Gib dann alle Namen in der Konsole aus. 
# Bsp.
# Luke Skywalker
# Anakin Skywalker
# ...

# Schreibe eine eigene Exception, um den Request sicher durchführen zu können.
# Den Request in ein try/except schreiben.

# Hausaufgabe (freiwillig):
# Schreibe eine Klasse Person, um die people in einem Objekt zu speichern.
# Die Klasse Person soll die vier Attribute name, height/groesse, mass/gewicht und haarfarbe/haircolor haben.
# Schreibe einen Konstruktor und eine String-Methode.
# Nutze zur Erstellung der Personen-Objekte eine Schleife.


# 1. Schritt: Daten aus der response in einer Datei speichern.
# 2. Schritt: Überpüfen, ob in der Datei schon Daten drin stehen, falls ja, keinen weiteres
# Get machen können. <-> Datei ist leer => Daten aus dem Internet lesen (und dann speichern)
# 3. Schritt: Weitere Datei erstellen und die Namen der Personen in der Datei speichern.
# Dateien öffnen und Dateien schließen.

class RequestException(Exception):
    def __str__(self):
        return "Beim Request ist ein Fehler aufgetreten."

def getAllNames():
    file = open('text.txt','r')
    if not file.read(): # Datei enthält keine Daten bzw ist leer # file.size()
        try:
            file.close()
            response = requests.get("https://swapi.dev/api/people/")
        except:
            print(RequestException())
        dict = response.json()
        listOfDicts = dict['results']
        file = open('text.txt','w')
        file.write(str(listOfDicts))
        file.close()
    else: # Datei enthält Daten
        file = open('text.txt', 'r')
        data = file.read() # Daten als String - wir brauchen: Daten, als Liste von Dict
        file.close()
        #print(json.loads(data))
    file.close()
        
    for l in listOfDicts:
        print(l['name'])

    # Schritt 3 wird morgen nachgeliefert :)

getAllNames()

# HTTP Status Codes:
# 2xx - alles okay 
# 4xx - Fehler auf Client-Seite
# 5xx - Fehler auf Server-Seite
# Alle weiteren hier: https://httpstat.us/

# zum Ausprobieren:
# print(response.text)
# print(response.content)
# print(response.json())
