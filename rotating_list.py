# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    for i in range(K):
        if A == []:
            return A
        A.insert(0, A.pop())
    return A


print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
print(solution([0], 4))