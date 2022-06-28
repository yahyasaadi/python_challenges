def isValid(s):
    
    strings = {'(':')', '{':'}', '[':']'}

    stack_list = []

    for open in s:
        if open in strings.keys():
            stack_list.append(open)
        elif stack_list == [] or open != strings[stack_list.pop()]:
            return False

    return stack_list == []



print(isValid('[]'))