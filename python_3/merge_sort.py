def merge(liste, linkeListe, rechteListe):
    indexLinkeListe = indexRechteListe = indexListe = 0

    while indexLinkeListe < len(linkeListe) and indexRechteListe < len(rechteListe):
        if linkeListe[indexLinkeListe] <= rechteListe[indexRechteListe]:
            liste[indexListe] = linkeListe[indexLinkeListe]                
            indexLinkeListe += 1
        else:
            liste[indexListe] = rechteListe[indexRechteListe]
            indexRechteListe += 1
        indexListe += 1

    while indexLinkeListe < len(linkeListe):
            liste[indexListe] = linkeListe[indexLinkeListe]
            indexLinkeListe += 1
            indexListe += 1

    while indexRechteListe < len(rechteListe):
            liste[indexListe] = rechteListe[indexRechteListe]
            indexRechteListe += 1
            indexListe += 1

    #print("Aktuelle sortierte Liste:", mainList)


def merge_sort(liste):
    if len(liste) < 2:  # Abbruchbedingung, um die Rekursion beenden zu können
        return liste
    mitte = len(liste) // 2

    #print("Aktuelle Liste: ", liste)

    linkeListe = liste[:mitte]
    rechteListe = liste[mitte:]

    #print("Aktuelle linke Liste: ", linkeListe)
    #print("Aktuelle rechte Liste", rechteListe)

    merge_sort(linkeListe)
    merge_sort(rechteListe)

    return merge(liste, linkeListe, rechteListe)

# Hausaufgabe: Den Mergesort zu Ende programmieren und verstehen :)