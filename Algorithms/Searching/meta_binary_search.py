# For meta binary search all data in variables must be sorted previously to work 
# algorithm properly.

import math
from string import ascii_lowercase

def meta_binary_search(arr, item):
    n = len(arr)
    lg = int(math.log2(n - 1)) + 1
    pos = 0
    
    for i in range(lg - 1, -1, -1):
        if arr[pos] == item:
            return f"The item '{arr[pos]}' was found at index {pos} in array {arr}"
        new_pos = pos | (1 << i)
        if new_pos < n and arr[new_pos] <= item:
            pos = new_pos
    return f"The item '{item}' is not presented in array {arr}"
    
if __name__ == "__main__":
 
    arr = sorted([ -2, 10, 100, 250, 32315, 234, 56, 23, 56, 23, 45, 56 ])
    item = 0
    letter = 's'
    print(meta_binary_search(arr, item))
    print(meta_binary_search(list(ascii_lowercase), letter))

