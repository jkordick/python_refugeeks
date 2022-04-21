#Mac: >>> pip3 install pandas
#Windows: >>> python3 -m pip install pandas

import pandas as pd
import numpy as np

"""
data = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

data_frame = pd.DataFrame(data)

print(data_frame)
"""

# Beispiel Series
#Zum erstellen von Series nutzen: Python Listen, 1-dimensionaleNumPyArrays und Konstanten
list = [1, 7, 2]
s = pd.Series(list)
#print(s)

s1 = pd.Series(1)
# print(s1)

s2 = pd.Series(np.array([1,2,3,4,5,6,7,8,9,10]))
# print(s2)
s2[0] # 1

# Labels
list = [1, 7, 2]
s = pd.Series(list, index = ["eins", "zwei", "drei"])
#print(s)
#print(s["zwei"]) #7

# Erstelle mehrere Series. Eine aus einem NumPy Array, eine aus einer Python Liste
# und eine aus einer Konstante. Gib mindestens einer Series Labels.

# Python Dictionary, um direkt Series mit Labels anlegen zu können.
students = {"001": "Julia", "002": "Kelvin", "003": "Melanie"}
s = pd.Series(students)
# print(s)

s1 = pd.Series(students, index = ["001", "002"])
# print(s1)

# Schreibt euch ein eigenes kleines Dictionary und macht aus diesem Dictionary
# eine Liste mit Labels.


# Erstelle einen eigenen DataFrame mit mindestens vier Series (Spalten) mit beliebigen
# Daten.

# Beispiel:
df = pd.DataFrame(
    {
         "Name": [
              "Braund, Mr. Owen Harris",
              "Allen, Mr. William Henry",
              "Bonnell, Miss. Elizabeth",
         ],
         "Age": [22, 35, 58],
         "Sex": ["male", "male", "female"],
         "Height": [176, 188, 190]
    }
)

# print(df)

# Aufgabe: Eine der beiden csv-Dateien aus dem Github 
# in unser Python Programm einlesen und sich die Daten ausgeben lassen.

# data_frame_countries = pd.read_csv('countries.csv')
# print(data_frame_countries)

data_frame_titanic = pd.read_csv('titanic.csv')
print(data_frame_titanic["Survived"].describe()) # 0 tot # 1 am Leben







