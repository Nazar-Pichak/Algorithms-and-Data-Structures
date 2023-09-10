# The Linear search in the Array Data Structure.
# In linear search, all items in array will be cheked on equality untill find the searching item,
# else 'item is not presented in array'.

def linear_search(arr: list, item: str):
    for i in range(len(arr)):
        if item == arr[i]:
            return f"The item {item} was found at index {i}"
    return f"The item {item} is not presented in array"

                    
if __name__ == '__main__':
    item = input("Enter your item: ")
    arr = list(input("Enter your array: "))
    print(linear_search(arr, item))