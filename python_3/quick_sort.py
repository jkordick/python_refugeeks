def quick_sort(start, end, liste):
    if (start < end):
        p = partition(start, end, liste)

        quick_sort(start, p - 1, liste)
        quick_sort(p + 1, end, liste)

def partition(start, end, liste):
    pivot_index = start
    pivot = liste[pivot_index]

    while start < end:
        while start < len(liste) and liste[start] <= pivot:
            start += 1

        while liste[end] > pivot:
            end -= 1

        if (start < end):
            liste[start], liste[end] = liste[end], liste[start]

        liste[end], liste[pivot_index] = liste[pivot_index], liste[end]

    return end
