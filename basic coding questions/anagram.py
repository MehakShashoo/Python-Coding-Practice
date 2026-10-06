# WAP to check if two strings are anagram
# Two strings are anagrams if they contain the same characters with the same frequency, but the order can be different. eg heart and earth

a = sorted(input("Enter first string: "))
b = sorted(input("Enter second string: "))

if a == b:
    print("Anagram")
else:
    print("Not anagram")