'''
Find largest without max()
Input a list and find the largest number using a loop.
'''

n = list(map(int,input("Enter your list: ").split()))
largest = float('-inf')
for i in n:
    if i>largest:
        lar = i
print(f"Largest number is {largest}")