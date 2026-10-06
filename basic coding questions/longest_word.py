'''
Write a program that:

takes a list of words from the user
finds the longest word
don't use max(..., key=len)

Example:
Input: apple banana cat watermelon mango
Output: watermelon

Hint: You'll need a variable to remember the longest word found so far.
'''

n = list((input("Enter your list: ").split()))
longest = n[0]
for i in n:
    if len(i) > len(longest):
        longest = i
print(f"Longest word is {longest}")
    