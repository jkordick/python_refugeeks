"""
dict = {
    "Name": "Julia",
    "Age": 31
}

print(dict["Age"])

del dict["Age"]

print(dict)

"""


# Schreibe ein Dictionary, das die folgenden Keys/Schlüssel enthält: Name, Alter, Wohnort
# Die zugehörigen Values/Werte sollen zunächst leere Strings sein.
# Schreibe eine Funktion die eine Eingabe des Wohnorts mit Hilfe von input erwartet und
# dann in dem Dictionary den Wohnort ändert.
# Gib das Dictionary dann in der Konsole aus.


# Erweitere die Funktion so, dass alle drei Elemente des Dictionaries, also auch Name und Alter
# mit Hilfe eines Inputs ersetzt werden können.
# Gib dann das Dictionary aus.
# Stelle sicher, dass das übergebene Dictionary die Elemente/Keys "Name", "Alter", "Wohnort" tatsächlich enthält.

# Verändere die Funktion so, dass für den Wohnort eine Liste von kompletten Adressen gespeichert wird.
# Bsp. "Wohnort" : ["Kleine Packhofstraße 16 30159 Hannover", "Bismarckstraße 10 30167 Hannover"]

# Verändere die Funktion so, dass ein Wohnort, als eine Liste von Listen gespeichert wird.
# Bsp: "Name" : [["Stefanie", "Müller"], ["Melanie", "Müller"]]
# oder
# Bsp.: "Wohnort" : [["Kleine Packhofstraße", "16", "30159", "Hannover"],["Bismarckstraße", "10", "30167", "Hannover"]]

personenDaten = {
    "Name": "",
    "Alter": "",
    "Wohnort": []
}

def dictManipulieren(dict): 
    i = 0
    while i < 100:
        strasse = input("Bitte gib deine Straße ein: ")
        hausNr = int(input("Bitte gib deine Hausnummer ein: "))
        plz = int(input("Bitte gib deine Postleitzahl ein: "))
        stadt = input("Bitte gib deine Stadt ein: ")
        adresse = [strasse, hausNr, plz, stadt]
        dict["Wohnort"].append(adresse)

        i += 1
        abbruchBedingung = input("Möchtest du eine weitere Adresse eingeben? (ja/nein) ")
        if abbruchBedingung == "nein":
            break
    return dict


""""
    #name = input("Bitte gib deinen Namen ein: ")
    #alter = int(input("Bitte gib dein Alter ein: "))

    for k in dict.keys():
        if k == "Name":
            dict["Name"] = name
        if k == "Wohnort":
             dict["Wohnort"] = wohnort
        if k == "Alter":
            dict["Alter"] = alter

            """



print(dictManipulieren(personenDaten))




