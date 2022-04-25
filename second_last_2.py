lst = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    nested_lst = [name, score]
    lst.append(nested_lst)
print(lst)