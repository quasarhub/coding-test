def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


array = [5, 2, 3, 7, 8, 1, 0, 4, 9, 6]
print(f"Original List       : {array}")
print(f"After Selection Sort: {selection_sort(array)}")

