# linear search on an array
arr = list(map(int,input("Enter elements: ").split()))
target = int(input("Enter the value to be searched: "))
found = 0
for i in arr:
    if arr[i] == target:
        print(f"Element found at index {i}")
        found = 1
        break
if found == 0:
    print("Element not found!")