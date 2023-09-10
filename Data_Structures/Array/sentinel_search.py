# The Sentinel search in Array Data Structure

def sentinel_search(arr, n, item):
    last = arr[n - 1]
    arr[n - 1] = item
    i = 0
    while arr[i] != item:
        i += 1
        
    arr[n - 1] = last
    
    if i < n - 1 or arr[n - 1] == item:
        return f"The item {item} was found at index {i}"
    return f'The item {item} is not presented in array'

item = 23
arr = [2, 4, 5, 6, 8, 2, 4, 5, 23]
n = len(arr)
print(sentinel_search(arr, n, item))