def binary_search(list, target):
    # print("value target: ", target)
    left = 0
    right = len(list) - 1
    while left <= right:
        # print("index left: ", left, " - index right: ", right)
        mid_point = (left + right) // 2
        # print("index mid_point: ", mid_point)
        if target < list[mid_point]:
            # print("value mid_point: ", list[mid_point], " > ", "value target: ", target)
            right = mid_point - 1
            # print("new index right: ", right)
        elif target > list[mid_point]:
            # print("value mid_point: ", list[mid_point], " < ", "value target: ", target)
            left = mid_point + 1
            # print("new index left: ", left)
        else:
            # print("target found! ", list[mid_point])
            return mid_point
    return -1

# Wir nehmen eine unsortierte Liste.
# Diese Liste sortieren wir mit dem bubble sort.
# In dieser sortierten Liste suchen wir mit Hilfe der binary search eine Zahl.
# Wir messen die Laufzeit unseres Programms.
# Wir gehen bei der binary search davon aus, dass die Liste sortiert ist.
# Stelle sicher, dass die Liste sortiert ist, indem du bubble sort und binary search so kombinierst.
# Mach am Ende Laufzeitmessung der kombinierten Funktionen.
