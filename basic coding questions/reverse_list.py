# Write a program that takes a list and creates a new reversed list.
'''
Rules:

Don't use [::-1]
Don't use .reverse()
Create a new list
'''
a = list(map(int,input("Enter your list: ").split()))
n = len(a)-1
new = []
for i in range(n , -1 , -1):
    new.append(a[i])
print(f"Reversed list is {new}")
