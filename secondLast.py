# Print names of second lowest grades and in alphabetical order
grades = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]


second_last = []
scores = set()
second_lowest_name = []
for n in range(len(grades)):
    scores.add(grades[n][1])

second_last = sorted(scores)[1]

ordered_names = []
for name, score in grades:
    if score == second_last:
        second_lowest_name.append(name)

for name in sorted(second_lowest_name):
    print(name, end='\n')



# Using List Comprehension
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))