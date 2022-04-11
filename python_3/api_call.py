import requests

response = requests.get("https://swapi.dev/api/people/1")

#API: application programming interface -> Anwendungsschnittstelle

print('Status Code:')
print(response.status_code)
print(response.text) # String
print(response.json()) # Dictionary

# Schreibe eine Funktion, die einen request durchführt, um mehrere people zu erhalten.
# Als request könnt ihr verwenden: https://swapi.dev/api/people/
# Gib dann alle Namen in der Konsole aus. 
# Bsp.
# Luke Skywalker
# Anakin Skywalker
# ...

# 2xx - alles okay 
# 4xx - Fehler auf Client-Seite
# 5xx - Fehler auf Server-Seite

# zum Ausprobieren:
# print(response.text)
# print(response.content)
# print(response.json())
