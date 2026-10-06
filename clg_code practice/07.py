'''
wap in python to input two lists and create a third list and create a third list containing common elements
'''
a = list(map(int,input("Enter elements of list 1: ").split()))
b = list(map(int,input("Enter elements of list 2: ").split()))
new = []

for i in a and b:
    if i in a and b:
        new.append(i)
print(new)
