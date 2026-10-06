'''
wap in python to input marks of n students in a list. Display the highest marks,lowest marks,average marks and number of students who passed.
'''
n = int(input("Enter number of students: "))
marks = list(map(int,input(f"Enter marks of {n} students: ").split()))
print(marks)
print("Highest marks: ",max(marks))
print("Lowest marks: ", min(marks))
print("Average marks: ", sum(marks)/n)

passed = 0

for i in marks:
    if i >= 40:
        passed = passed + 1
print(f"Number of students passed is {passed}")