def to_underscore(string):
    string = str(string)
    snake_case = string[0].lower()

    for s in string[1:]:
        snake_case += f"_{s.lower()}" if s.isupper() else s

    return snake_case

print(to_underscore("yahyaSaadiNoor"))
print(to_underscore("App7Test"))
print(to_underscore(4))