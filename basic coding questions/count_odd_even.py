'''
Count even and odd numbers
Input a list and count how many numbers are even and how many are odd.
'''

n = list(map(int,input("Enter your list: ").split()))
odd = 0
even = 0
for i in n:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f"Count of even number is {even} and count of odd number is {odd}")