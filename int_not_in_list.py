# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    len_of_list = len(A)
    set_a = set(A)
    
    for i in range(1, len_of_list + 2):
        if i not in set_a:
            return i


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([40, 89, 90, 105]))
print(solution([1, 2, 3]))
print(solution([-1, -2, -3]))
print(solution([1, 2, 3, 4, 5, 6, 8, 9]))

