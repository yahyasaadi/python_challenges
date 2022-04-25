def fizzBuzz(number):
    for num in range(number):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


# fizzBuzz(20)

# func move letters x amount of indices
def rotate(my_list, num_rotations):
    for i in range(num_rotations):
        my_list.insert(0, my_list.pop())
    return my_list

print(rotate(['a', 'b', 'c', 'd'], 2))