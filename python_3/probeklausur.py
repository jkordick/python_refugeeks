# 1) 
import requests

def getPeople():
    try:
        response = requests.get("https://swapi.dev/api/people")
    except: 
        raise Exception()
    else:
        return response.text

print(getPeople())

# Exception zu verwenden und den request in ein try/except oder try/catch setzen

# 2)
# positiv: 200, 201
# negativ: 400, 404, 500, 503

# 3) Bubble-Sort, Merge-Sort, Quick-Sort, Lineare Suche, Binäre Suche

# 4) O(1) < O(n) < O(n log n) < O(n^2) < O(2^n)

# 5)linear_search([1, 2, 3], 3) # Liste soll sortiert sein!

# 6) Sortieralgorithmus, 
# benachbarte Elemente wiederholt tauschen, 
# wiederholt bis alles sortiert ist
# schleche Laufzeit 0(n^2)
# laufen wiederholt vollständig durch die Liste, 
# bis keine Elemente mehr getauscht werden,
# und die Liste dann vollständig sortiert ist

# 7) Funktion, die sich selbst aufruft, so lange, bis eine Abbruchbedinung wahr wird/erfüllt ist

# 8) [[9,8], [7,6], [5,4], [3,2]]

# 9) 
# Unterschiede:
# NumPy-Array ist (50-Mal) schneller als eine Python Liste
# NumPy-Array kann mehrere Dimensionen haben, eine Python Liste ist immer nur 1-dimensional
# NumPy-Array hat mehr Hilfsfunktionen, um die Daten zu verändern
# NumPy-Arrays sollen möglichst homogen sein, Listen können auch heterogene Daten enthalten

# Gemeinsamkeiten:
# Slicing
# Zugriff auf Werte über Indexe
# können beide zum Erstellen von Series verwendet werden

# 10) Data-Frame, Series



