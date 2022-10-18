"""
    - Get all ints that are multiples of 3
    - Then return the max int
"""

def solution(A):
    return max([A[i] for i in range(len(A)) if A[i] % 3 == 0])


print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
print(solution([3, 6, 9, 12, 15, 18, 21, 24, 27, 30]))