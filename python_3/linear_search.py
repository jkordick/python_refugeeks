def linear_search(list, x):
    for i in list:
        if list[i] == x:
            return i
    return -1
