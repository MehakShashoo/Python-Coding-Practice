n = list(map(int,input("Enter your list: ").split()))
lar = float('-inf')
sec_lar = float('-inf')
for i in n:
    if i > lar:
        lar = i
        sec_lar = lar
    elif i > sec_lar and lar != sec_lar:
        sec_lar = i
print(f"Second largest number is {sec_lar}")