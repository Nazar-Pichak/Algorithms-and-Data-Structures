# Iterative Binary search in array.
# To apply Binary Search algorithm:
# - The data structure must be sorted.
# - Access to any element of the data structure takes constant time.

def iterative_binary_search(arr, left, right, item):
    
    while left <= right:
        midle = left + (right - 1) // 2
        if arr[midle] == item:
            return f"The item {arr[midle]} was found at index {midle}"
        if arr[midle] < item:
            left = midle + 1
        else:
            right = midle - 1
    return 'The item is not presented in array'


def recursive_binary_search(arr, left, right, item):
    pass

           
arr = sorted(list(input('Enter your array: ')))
item = input('Enter your item: ')
print(iterative_binary_search(arr, 0, len(arr) - 1, item))
