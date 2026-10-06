#Print the fibonacci series
#A Fibonacci series is a sequence where each number is the sum of the previous two numbers.

n = int(input("Enter number of terms: "))
if n < 0:
    print("Invalid")
elif n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a = 0
    b = 1
    print(a,b,end = " ")
    for i in range(n-2):
        c = a + b
        print(c,end = " ")
        a = b
        b = c