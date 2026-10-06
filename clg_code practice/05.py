'''
wap in python to input numbers in a list and create two separate lists for even and odd numbers
''' 
n = list(map(int,input("Enter numbers: ").split()))
even = []
odd = []

for i in n:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)
print(f"Even number list: {even} ")
print(f"Odd number list: {odd}")