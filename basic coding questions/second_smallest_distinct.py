'''
Given a list of integers, find the second smallest distinct element.

Example:
Input:  8 3 1 6 3 9 1 5
Output: 3

Because the distinct values are:
1, 3, 5, 6, 8, 9
'''

n = list(map(int,input("Enter your list: ").split()))
distinct_list = []
for i in n:
    if i not in distinct_list:
        distinct_list.append(i)
print(f"List with distinct elements are {distinct_list}")

small = float('inf')
sec_small = float('inf')

for i in distinct_list:
    if i < small:
        sec_small = small
        small = i
    elif i < sec_small and i != small:
        sec_small = i

print(f"Second smallest element from distinct list is {sec_small}")
