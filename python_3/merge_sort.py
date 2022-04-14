def merge(mainList, leftList, rightList):
    indexLeft = indexRight = indexMain = 0

    while indexLeft < len(leftList) and indexRight < len(rightList):
        if leftList[indexLeft] <= rightList[indexRight]:
            mainList[indexMain] = leftList[indexLeft]                
            indexLeft += 1
        else:
            mainList[indexMain] = rightList[indexRight]
            indexRight += 1
        indexMain += 1

    while indexLeft < len(leftList):
            mainList[indexMain] = leftList[indexLeft]
            indexLeft += 1
            indexMain += 1

    while indexRight < len(rightList):
            mainList[indexMain] = rightList[indexRight]
            indexRight += 1
            indexMain += 1

    print("Aktuelle sortierte Liste:", mainList)


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


merge_sort([54,26,93,17,77,31,44,55,20])

# Hausaufgabe: Den Mergesort zu Ende programmieren und verstehen :)