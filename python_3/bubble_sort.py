def bubble_sort(liste): 
    n = len(liste)
    #print("Start: ", liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
        # Tauschen der Elemente
            #print("Index: ", j, " - 1. Wert: " , liste[j], " - 2. Wert: ", liste[j + 1])
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                #print("Werte wurden getauscht!")
                #print("Neues Array: ", liste)
           # else: 
                #print("Werte wurden nicht getauscht!")
                #print("Neues Array: ", liste)
    #print("Ende: ", liste)
    return liste