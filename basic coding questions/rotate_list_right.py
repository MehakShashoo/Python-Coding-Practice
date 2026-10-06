# Write a Python program to rotate a list one position to the right.
n = list(map(int,input("Enter your list: ").split()))
last_ele = n.pop()
n.insert(0,last_ele)
print(f"Rotated list is {n}")