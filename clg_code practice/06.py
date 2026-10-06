'''
wap in python to rotate a list one position to the right
'''
n = list(map(int,input("Enter your list: ").split()))
last_digit = n.pop()
n.insert(0,last_digit)
print(f"Rotated list is {n}")