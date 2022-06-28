
n = 2
student_marks = {}

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("Name to query: ")
marks = student_marks[query_name]
avg = 0
total = 0
for mark in marks:
    total += mark
    
    # print(mark)
    
avg = total/len(marks)
print(avg)
# print(len(marks))