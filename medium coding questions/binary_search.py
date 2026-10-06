# Search on an array using binary search 
# Binary search always works on a sorted array
arr = list(map(int,input("Enter elements: ").split()))
arr.sort()
print(f"Sorted array:{arr}")
target = int(input("Enter element to be searched: "))
left = 0
right = len(arr) - 1
found = 0

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Element found at index {mid}")
        found = 1
        break
    elif arr[mid] < target:
        left = mid + 1
    else :
        right = mid - 1
if found == 0:
    print("Element not found!!")