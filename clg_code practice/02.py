'''
wap in python to input marks of 10 students. Store only valid marks between 0 and 100 in a list. Skip invalid marks.
'''
marks = list(map(int,input("Enter marks of 10 students: ").split()))
valid_marks = []
for i in marks:
    if i >= 0 and i <= 100:
        valid_marks.append(i)
print(valid_marks)