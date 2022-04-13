def merge_sort(list):
    if len(list) < 2:  # Abbruchbedingung, um die Rekursion beenden zu können
        return list
    middle = len(list) // 2

    print("Aktuelle Liste: ", list)

    leftList = list[:middle]
    rightList = list[middle:]

    print("Aktuelle linke Liste: ", leftList)
    print("Aktuelle rechte Liste", rightList)

    merge_sort(leftList)
    merge_sort(rightList)

    #return merge(list, leftList, rightList)

merge_sort([54,26,93,17,77,31,44,55,20])