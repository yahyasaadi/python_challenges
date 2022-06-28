def solution(roman):
    numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    the_int = 0
    for i in range(len(roman)):
        if i > 0 and numeral[roman[i]] > numeral[roman[i-1]]:
            the_int += numeral[roman[i]] - 2 * numeral[roman[i-1]]
        else:
            the_int += numeral[roman[i]]
    return the_int

print(solution('IV'))
print(solution('V'))
# numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# rom = 'IV'
# print(numeral[rom[0]])