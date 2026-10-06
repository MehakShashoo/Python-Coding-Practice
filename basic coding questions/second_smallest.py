#Print the second smallest number in a list

n = list(map(int,input("Enter your list: ").split()))
small = float('inf')
sec_small = float('inf')
for i in n:
    if i < small:
        small = sec_small
        small = i
    elif i < sec_small and i != small:
        sec_small = i
print(f"Second smallest number in list is {sec_small}")