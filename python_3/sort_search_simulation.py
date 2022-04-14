# Schreibe ein Programm, das alle Sortier und Suchalgorithmen, die wir
# kennen gelernt haben, enthält. (Lineare Suche, Binäre Suche, BubbleSort, MergeSort, QuickSort)
# Diese müssen alle, in einzelnen Funktionen sein, damit wir diese aufrufen können.
# Steuert über einen input, welchen Such und/oder Sortieralgorithmus, ihr verwenden möchtest.
# Für jeden Simulationsdurchlauf eine Zeitmessung machen.
# Bsp.:
# Welcher Algorithmus soll verwendet werden?
# Eingabe: Bubble
# BubbleSort wurde durchgeführt mit folgender Liste: [xxx]
# Die Laufzeit war: 0.32323232 Sekunden
#
# 1.Schritt: Einzelne Algorithmen. Nicht vergessen: Wenn wir suchen, müssen wir das Suchelement 
# eingeben können.
# 2. Schritt: Kombinationen von Algorithmen. Bsp.: 1. Quicksort 2. Binäre-Suche
# 3. Schritt: Achtung, eigene Recherche :) Finde heraus, wie die Listen, die wir für die Suche/das Sortieren nutzen
# randomisiert generiert werden können. Erweitere die Simulation um folgende Abfrage:
# Wie viele Elemente soll die Liste enthalten?
# Eingabe: 1000
# Der BubbleSort wurde durchgeführt mit einer Liste mit 1000 Elementen.
# Die Laufzeit war: 0.43232 Sekunden

# Wie machen wir die Interaktion Mensch <-> Computer?
# Wie entscheide ich nach der Eingabe, welchen Algorithmus bzw. welche Funktion ich aufrufen muss?
# Wie und wo messe ich die Zeit, damit es immer für jede Kombination funktioniert?

import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort


def algorithmusAuswahl():
    liste = [54,26,93,17,77,31,44,55,20]
    eingabe = input("Welcher Algorithmus soll verwendet werden?")

    begin = time.time()
    if eingabe == "Bubble":
        bubble_sort(liste)
    elif eingabe == "Merge":
        merge_sort(liste)
    elif eingabe == "Quick":
        quick_sort(liste)
    else:
        print("Es wurde keine Eingabe gemacht")

    end = time.time()

    print ("Das Programm lief : " + str(end-begin) + " Sekunden")

algorithmusAuswahl()