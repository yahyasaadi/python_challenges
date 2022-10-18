"""
    https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
"""

def plusMinus(arr):
    # Write your code here
    positives, zeros, negatives = 0, 0, 0
    for i in arr:
        if i > 0:
            positives += 1
        elif i == 0:
            zeros += 1
        else:
            negatives += 1
    
    print('{0:.6f}'.format(positives/len(arr)))
    print('{0:.6f}'.format(negatives/len(arr)))
    print('{0:.6f}'.format(zeros/len(arr)))
 
   

plusMinus([-4, 3, -9, 0, 4, 1])
plusMinus([1, 1, 0, -1, -1])

