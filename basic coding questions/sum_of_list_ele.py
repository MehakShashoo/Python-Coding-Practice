'''
Sum of list elements
Input a list of numbers and find the sum of all elements.
'''

n = list(map(int,input("Enter your list: ").split()))
sum = 0
for i in n:
    sum = sum + i
print(f"Sum of elements are {sum}")