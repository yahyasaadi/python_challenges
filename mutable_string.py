def mutate_string(string, position, character):
    l_string = list(string)
    l_string[position] = character
    string = ''.join(l_string)
    return string


print(mutate_string('Yahya', 4, 'u'))