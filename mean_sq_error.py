'''
https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python
'''

def solution(array_a, array_b):
    squares = [abs(array_a[i] - array_b[i])**2 for i in range(len(array_a))]
    return sum(squares)/len(squares)

print(solution([1,2,3], [4,5,6]))
print(solution([10, 20, 10, 2], [10, 25, 5, -2]))

"""
Inputs and desired outcomes

[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2

"""