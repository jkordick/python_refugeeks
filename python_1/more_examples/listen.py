list = ["python", "refugeeks", "I am a string!"]

# zugriff auf einen Index (Indizes starten bei 0!)

print(list[0])  # python

print(list[2])  # I am a string!

print(list[1:2])  # slicing

new_list = [[True, False, True], [25, 63, 23]]
print(new_list[0][2])

list[1] = 'Apple'
print(list)  # ["python", "Apple", "I am a string!"]

a = [1, 6, 2]
b = [5, 2, 6]
c = a + b
print(c)  # [1, 6, 2, 5, 2, 6]
d = c * 2
print(d)  # [1, 6, 2, 5, 2, 6, 1, 6, 2, 5, 2, 6]


# Hilfsmethoden
list = ["python", "refugeeks", "I am a string!"]
list.append('Apple')
print(list)  # ["python", "Apple", "I am a string!", "Apple"]

a = [1, 6, 2]
b = [5, 2, 6]
a.extend(b)
print(a)  # [1, 6, 2, 5, 2, 6]

list = ["a", "b", "c"]
list.pop(1)
print(list)  # ["a", "c"]

list = ["a", "b", "c"]
list.remove("c")
print(list)  # ["a", "b"]

list = ["a", "b", "c", "d"]
del(list[1:3])
print(list)  # ["a", "d"]

list = [5, 3, 1]
list.sort()
print(list)  # [1, 3, 5]

list = [5, 3, 1]
print(len(list))  # 3


# Tupel
tuple = ("python", "refugeeks", "I am a string!")

tuple[2] = "Test"  # Fehler: TypeError


# Dict
dict = {
    "name": "Julia",
    "job": "Software Engineer",
    "degrees": ["B. Sc.", "M. Sc."]
}

print("dict['Name']: ", dict['name'])  # Julia
print("dict['Job']: ", dict['job'])  # Software Engineer


dict['name'] = "Kelvin" # Eintrag ändern
del dict['name']; # Eintrag 'name' löschen
dict.clear();     # Alle Einträge löschen
