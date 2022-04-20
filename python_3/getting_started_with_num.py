# Mac: >>> pip3 install numpy
# Windows: >>> python3 -m pip install numpy

from statistics import mean
from turtle import goto
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

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:4])
# print(arr[5:])
# print(arr[-5:-1]) # wenn ich die letzten 4 Elemente meines Arrays finden möchte (exclusive des letzten Elements)

# Wie nutzen wir Slicing bei 2-dimensionalen Arrays?
# Gegeben ist folgendes n-dimensionales Array: [[6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]
# Lass dir [3, 4] ausgeben.
# Lass dir [7, 8] und [1, 2, 3] ausgeben.
# Lass dir aus beiden Arrays den Index [3] ausgeben.
# Lass dir aus beiden Arrays die Indexe [1] bis [3] ausgeben.
# Lass dir aus dem ersten Array die Indexe [0] bis [3] ausgeben.

"""
arr = np.array([[6, 7, 8, 9, 10], [1, 2, 3, 4, 5]])
print(arr[1, 2:4])
print(arr[0, 1:3], arr[1, 0:3])
print(arr[0:, 3])
print(arr[0:, 1:4])
print(arr[0, 0:4])
"""

# Python-Datentypen, die wir bereits kennengelernt haben:
# string, integer, float, boolean, none

# NumPy Datentypen:
# i - integer (8 bis 64-Bit)!
# b - boolean!
# u - unsigned integer
# f - float!
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string!
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# ndarray = np.array([1, 2, 3], dtype='f') # oder dtype='i4' oder np.int32 4-Byte = 32-Bit
# print(ndarray.dtype)
# print(ndarray)

#arr = np.array([1.1, 2.1, 3.1])
#print("Alter Typ:", arr.dtype)
#newarr = arr.astype('i8')
#print(newarr)
#print("Neuer Typ:", newarr.dtype)
"""
arr = np.array(["name", "hallo", "welt"])
print("Alter Typ:", arr.dtype)
newarr = arr.astype('i8')
print(newarr)
print("Neuer Typ:", newarr.dtype)

arr = np.array(["1", "2", "3"])
print("Alter Typ:", arr.dtype)
newarr = arr.astype('i8')
print(newarr)
print("Neuer Typ:", newarr.dtype)

arr = np.array(["name", "hallo", "welt"])
print("Alter Typ:", arr.dtype)
newarr = arr.astype('i8')
print(newarr)
print("Neuer Typ:", newarr.dtype)


arr = np.array([1, 0, 3, -1, 1.1]) # 0 = False # != 0 = True
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# Schreibe ein Programm, dass dir jedes Element einzeln ausgibt.
# Das Ergebnis soll sein:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

for i in arr:
    for j in i:
        print(j)


arr2 = np.array([[5, 4, 3, 2, 1], [6, 7, 8, 9, 10]])

print(arr2.mean())
print(arr2.max())
print(arr2.min())
print(arr2.sort())
print(arr2)

arr1 = np.array([7, 2, 5, 4, 3, 6, 1])
print(arr1.mean())
print(arr1.max())
print(arr1.min())
print(arr1.sort())
print(arr1)

arrS = np.array(["hallo", "hello", "welt", "num", "py", 5, 10, 1, 2])
# print(arrS.mean()) # !
# print(arrS.max())
# print(arrS.min())
print(arrS.sort())
print(arrS)


arr1S = np.array(['7', '2', '5', '4', '3', '6', '1']) # funktioniert auch :)

print(arr1S, arr1, arr2) # print() 1. Parameter Pflicht, 2. + n Parameter Optional
#[Startindex:Endindex]
#[Startindex:(Step/Schrittweite:)Endindex]

"""
arr0 = np.array([[3, 4], [1, 2], [9, 10]])
arr1 = np.array([[5, 6], [7, 8], [11, 12]])

#print(np.concatenate((arr0, arr1), axis=None))
#print(np.concatenate((arr0, arr1), axis=0))
#print(np.concatenate((arr0, arr1), axis=1))

print(arr0.shape) # Tupel der Array-Dimensionen.
print(arr0.ndim) # Anzahl der Array-Dimensionen
print(arr0.size) # Anzahl Elemente im Array
print(arr0.itemsize) # Speichergröße eines einzelnen Elements in bytes
print(arr0.nbytes)

# Schreibe eine Funktion, die zwei Übergabeparameter akzeptiert (arr0, arr1).
# Prüfe, ob die beiden Arrays die gleiche Größe haben. Erinnerung: mit arr.size können wir die Größe prüfen
# Wenn die Arrays gleich groß sind print("Gleich groß"), wenn nicht print("Nicht gleich groß")














