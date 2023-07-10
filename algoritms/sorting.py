def selectionSort(arr) -> list:
    lenght_array = len(arr)
    for i in range(lenght_array-1):
        min_value = arr[i]
        min_index = i
        for j in range(i+1, lenght_array):
            if min_value > arr[j]:
                min_value = arr[j]
                min_index = j
        if min_index != i:
            t = arr[i]
            arr[i] = min_value
            arr[min_index] = t
    return arr
# O(n**2)


def insertingSort(arr):
    lenght_array = len(arr)
    for i in range(1, lenght_array):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1],  arr[j]
            else:
                break
    return arr
# O(n**2)


def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr
# O(n**2)


def quickSort(array):
    if len(array) <= 1:
        return array
    pivotIndex = len(array) // 2
    pivot = array[pivotIndex]
    less = []
    greater = []
    for i in range(len(array)):
        if i == pivotIndex:
            continue
        elif array[i] < pivot:
            less.append(array[i])
        else:
            greater.append(array[i])
    return [*quickSort(less), pivot, *quickSort(greater)]
# O(log n * n)f


print(quickSort([9, 0, 7, 5, 4, 3, 2]))
print(insertingSort([9, 0, 7, 5, 4, 3, 2]))
print(bubbleSort([9, 0, 7, 5, 4, 3, 2]))
print(selectionSort([9, 0, 7, 5, 4, 3, 2]))
