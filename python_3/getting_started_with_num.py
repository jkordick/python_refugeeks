# Mac: >>> pip3 install numpy
# Windows: >>> python3 -m pip install numpy

import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# Gegeben ist folgendes n-dimensionales Array: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# Lass dir die Nummer 8 ausgeben. 
# Lass dir die Nummer 2 ausgeben.
# Lass dir das letzte Element der zweiten Dimension ausgeben. # Recherche :)

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 2])
# print(arr[0, 1])
# print(arr[1, -1])

# Gegeben ist folgendes n-dimensionales Array: [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
# Lass die die Nummer 7 ausgeben.
# Welche Nummer wird mit dem folgenden Aufruf arr[1, 0, 2] ausgegeben?
# Lass dir die Nummer 11 ausgeben.
# Welche Nummer wird mit dem folgenden Aufruf arr[0, 0, 1] ausgegeben?
# Addiere die Werte an den Indexen [0, 1, 0] und [1, 1, 0] - welches Ergebnis kommt dabei heraus?

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[1, 0, 0])
# print(arr[1, 0, 2])
# print(arr[1, 1, 1])
# print(arr[0, 0, 1])
# print(arr[0, 1, 0] + arr[1, 1, 0]) # 4 + 10

# Gegeben ist folgendes n-dimensionales Array: [1, 2, 3, 4]
# Lass dir die Nummer 2 ausgeben.
# Lass dir die Nummer 1 ausgeben.
# Addiere die Werte an den Indexen [1] und [2] - welches Ergebnis kommt dabei heraus?

# arr = np.array([1, 2, 3, 4])
# print(arr[1])
# print(arr[0])
# print(arr[1] + arr[2])

# Wiederholung Slicing
# Erinnerung: Das Ergebnis enthält den Startindex, jedoch nicht den Endindex. 

# Gegeben ist folgendes n-dimensionales Array: [1, 2, 3, 4, 5, 6, 7]
# Wie muss ich Slicing anwenden, um das Ergebnis [2, 3, 4] zu erhalten?
# Wie muss ich Slicing anwenden, um das Ergebnis [6, 7] zu erhalten?
# Beispiel für negatives Slicing: [-5:-1] - was ist das Ergebnis?

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:4])
print(arr[5:])
print(arr[-5:-1]) # wenn ich die letzten 4 Elemente meines Arrays finden möchte (exclusive des letzten Elements)

# Wie nutzen wir Slicing bei 2-dimensionalen Arrays?
# Gegeben ist folgendes n-dimensionales Array: [[6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]
# Lass dir [3, 4] ausgeben.
# Lass dir [7, 8] und [1, 2, 3] ausgeben.
# Lass dir aus beiden Arrays den Index [3] ausgeben.
# Lass dir aus beiden Arrays die Indexe [1]-[3] ausgeben.
# Lass dir aus dem ersten Array die Indexe [0]-[3] ausgeben.


