list1 = [1, 2, 3, 4, 5]


def reverse_fun(numbers):
    if len(numbers) == 1:
        return numbers
    # Otherwise
    return reverse_fun(numbers[1:]) + numbers[0:1]


print(reverse_fun(list1))