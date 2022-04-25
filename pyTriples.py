# Function to check for Pythegoram Triples
def pyCheck(lst):
    lst.sort()
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if (lst[i]**2 + lst[j]**2 == lst[k]**2):
                    return True
    return False



print(pyCheck([3, 4, 5]))
print(pyCheck([12, 10, 11, 72]))
print(pyCheck([5, 4, 3]))