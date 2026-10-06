'''
wap in python to input numbers in a list and find the second largest number.
'''
n = list(map(int,input("Enter numbers: ").split()))
lar = float('-inf')
sec_lar = float('-inf')
for i in n:
    if i > lar:
        sec_lar = lar
        lar = i
    elif i > sec_lar and i != lar:
        sec_lar = i
print(f"Second largest number is {sec_lar}")