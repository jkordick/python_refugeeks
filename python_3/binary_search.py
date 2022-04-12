def binary_search(arr, target):
    print("value target: ", target)
    left = 0
    right = len(arr) - 1
    while left <= right:
        print("index left: ", left, " - index right: ", right)
        mid_point = (left + right) // 2
        print("index mid_point: ", mid_point)
        if target < arr[mid_point]:
            print("value mid_point: ", arr[mid_point], " > ", "value target: ", target)
            right = mid_point - 1
            print("new index right: ", right)
        elif target > arr[mid_point]:
            print("value mid_point: ", arr[mid_point], " < ", "value target: ", target)
            left = mid_point + 1
            print("new index left: ", left)
        else:
            print("target found! ", arr[mid_point])
            return mid_point
    return -1

binary_search([1,6,10,20,23,29,33,37,42,47,50,55,60,74,86,100], 33)

# Wir gehen bei der binary search davon aus, dass die Liste sortiert ist.
# Stelle sicher, dass die Liste sortiert ist, indem du bubble sort und binary search so kombinierst.
# Mach am Ende Laufzeitmessung der kombinierten Funktionen.
