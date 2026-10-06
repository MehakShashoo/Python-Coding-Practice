'''
wap in python to create a list of numbers and create a new list containing only unique elements
'''

n = list(map(int,input("Enter your list: ").split()))
new = []
for i in n:
    if i not in new:
        new.append(i)
print(new)