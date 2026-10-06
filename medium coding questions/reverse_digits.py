# Write a program that reverses the digits of an integer.

# If you extract a digit, how can you build a new number by putting that digit at the end?
n = int(input("Enter number:"))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print(f"Reverse of these number is {reverse}")