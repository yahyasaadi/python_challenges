def split_and_join(line):
    # write your code here
    split_line = line.split(" ")
    return "-".join(split_line)


print(split_and_join('this is a string'))