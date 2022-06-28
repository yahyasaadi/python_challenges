def is_narcissistic(i):
    numbers = str(i)
    return sum(int(num) ** len(numbers) for num in numbers) == i


print(is_narcissistic(153))
print(is_narcissistic(1634))
print(is_narcissistic(407))
print(is_narcissistic(259))