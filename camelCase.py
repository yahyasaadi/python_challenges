def splitString(word):
    return ''.join([' '+ c if c.isupper() else c for c in word])


print(splitString("jasonBourne"))
print(splitString("donaldJTrump"))