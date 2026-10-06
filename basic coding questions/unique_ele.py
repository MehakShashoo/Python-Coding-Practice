'''
Write a Python program that:

takes a list of integers from the user
creates a new list containing only unique elements
preserves their original order
'''

n = list(map(int,input("Enter your list: ").split()))
new = []
for i in n:
    if i not in new:
        new.append(i)
print(f"List with no duplicates is {new}")