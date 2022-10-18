"""
    https://www.hackerrank.com/challenges/merge-the-tools/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign

"""
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        unique = ''
        for j in string[i : i+k]:
            if j not in unique:
                unique+=j
        print(unique)


merge_the_tools('AABCAAADA', 3) 
