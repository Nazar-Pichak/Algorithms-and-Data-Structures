# The ternary seach also requires an sorted array to work algorithm properly.

def recursive_ternary_search(left, right, item, arr):
    
    if right >= left:
        mid_one = left + (right - left) // 3
        mid_two = right - (right - left) // 3
        
        if arr[mid_one] == item:
            return f"The item {arr[mid_one]} was found at index {mid_one}"
        if arr[mid_two] == item:
            return f"The item {arr[mid_two]} was found at index {mid_two}"
        
        if item < arr[mid_one]:
            return recursive_ternary_search(left, mid_one - 1, item, arr)
        elif item > arr[mid_two]:
            return recursive_ternary_search(mid_two + 1, right, item, arr)
        else:
            return recursive_ternary_search(mid_one + 1, mid_two - 1, item, arr)
        
    return f"The item {item} was not found in array {arr}"


def iterative_ternary_search(left, right, item, arr):
    
    while right >= left:
        mid_one = left + (right - left) // 3
        mid_two = right - (right - left) // 3
        
        if arr[mid_one] == item:
            return f"The item {arr[mid_one]} was found at index {mid_one}"
        if arr[mid_two] == item:
            return f"The item {arr[mid_two]} was found at index {mid_two}"

        if item < arr[mid_one]:
            right = mid_one - 1
        elif item > arr[mid_two]:
            left = mid_two + 1
        else:
            left = mid_one + 1
            right = mid_two - 1
        
    return f"The item {item} was not found in array {arr}"
        

item = input('Enter your item: ')
arr = list(input('Enter your array: '))

print(recursive_ternary_search(0, len(arr), item, sorted(arr)))
print(iterative_ternary_search(0, len(arr), item, sorted(arr)))