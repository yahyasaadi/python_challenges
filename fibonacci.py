a, b = 0, 1

for i in range(1, 10):
    print(a)
    a, b = b, a + b

print('//////')
# My way
a, b = 0, 1

for i in range(10):
    print(a)
    a, b = a+b, a