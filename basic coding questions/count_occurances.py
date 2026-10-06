'''
Write a program that:

takes a list from the user
asks the user for an element
counts how many times that element appears in the list
don't use .count()
'''

n = list(map(int,input("Enter your list: ").split()))
ele = int(input("Enter the value to be counted: "))
count = 0
for i in n:
    if i == ele:
        count = count + 1
print(f"The element {ele} occurred {count} times")