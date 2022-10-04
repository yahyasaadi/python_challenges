# https://www.hackerrank.com/challenges/compare-the-triplets/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

#!/bin/python3

import os

# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    
    for al, bo in zip(a, b):
        if al > bo:
            alice+=1
        elif bo > al:
            bob+=1
    return f'{alice} {bob}'
             
    
    
if __name__ == '__main__':
    

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
