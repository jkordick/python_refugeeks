import requests

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

class RequestException(Exception):
    def __str__(self):
        return "Beim Request ist ein Fehler aufgetreten."

def getAllNames():
    try:
        response = requests.get("https://swapi.dev/api/people/")
    except:
        print(RequestException())
    dict = response.json()
    listOfDicts = dict['results']

    for l in listOfDicts:
        print(l['name'])



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
