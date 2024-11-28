def selection_sort(array):
    for i in range(len(array) - 1):
        index_minima = i
        for j in range(i + 1, len(array)):
            if array[j] < array[index_minima]:
                index_minima = j

        array[i], array[index_minima] = array[index_minima], array[i]
    return array

print(selection_sort([5, 8, 6, 4, 7, 1, 3, 2]))