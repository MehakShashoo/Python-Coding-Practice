# Write a Python program that takes an integer and calculates the sum of all its digits.
n = int(input("Enter number: "))
count = 0
while n > 0:
    digit = n % 10
    count = count + digit
    n = n // 10
print(f"Sum of digits are {count}")