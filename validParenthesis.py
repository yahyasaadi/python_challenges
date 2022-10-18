'''
https://leetcode.com/problems/valid-parentheses/
'''

def isValid(s):
    """function checking for valid parenthesis

    Args:
        s (string): eg: '[]', ']][['

    Returns:
        boolean: func returns True if all parenthesis are valid, else False
    """
    
    strings = {'(':')', '{':'}', '[':']'}

    stack_list = []

    for open in s:
        if open in strings.keys():
            stack_list.append(open)
        elif stack_list == [] or open != strings[stack_list.pop()]:
            return False

    return stack_list



print(isValid('[]'))