def bubbleSort(array): 
    n = len(array)
    print("Start: ", array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
        # Tauschen der Elemente
            print("Index: ", j, " - 1. Wert: " , array[j], " - 2. Wert: ", array[j + 1])
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print("Werte wurden getauscht!")
                print("Neues Array: ", array)
            else: 
                print("Werte wurden nicht getauscht!")
                print("Neues Array: ", array)
    print("Ende: ", array)


bubbleSort([6,7,3,4,6,1,2])