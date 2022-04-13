def merge_sort(liste):
    if len(liste) < 2:  # Abbruchbedingung, um die Rekursion beenden zu können
        return liste
    mitte = len(liste) // 2

    print("Aktuelle Liste: ", liste)

    linkeListe = liste[:mitte]
    rechteListe = liste[mitte:]

    print("Aktuelle linke Liste: ", linkeListe)
    print("Aktuelle rechte Liste", rechteListe)

    merge_sort(linkeListe)
    merge_sort(rechteListe)

    #return merge(list, leftList, rightList)

merge_sort([54,26,93,17,77,31,44,55,20])

# Hausaufgabe: Den Mergesort zu Ende programmieren und verstehen :)