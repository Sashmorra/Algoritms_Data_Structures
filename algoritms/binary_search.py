def binarySearch(array, item):
    start = 0
    end = len(array)
    middle = 0
    found = False
    position = -1
    while found == False or start <= end:
        middle = (start + end)//2
        if array[middle] == item:
            found = True
            position = middle
            return position
        elif array[middle] < item:
            start = middle + 1
        else:
            end = middle - 1

    return position


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 7))
# O(log n)
