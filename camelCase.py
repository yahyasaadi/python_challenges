def splitString(word):
    # lst_word = []

    # for letter in word:
    #     if letter.isupper():
    #         lst_word.append(' '+letter)
    #     else:
    #         lst_word.append(letter)
    # return ''.join(str(e) for e in lst_word)
    return ''.join([' '+ c if c.isupper() else c for c in word])


# splitString("yahyaSaadi")
print(splitString("yahyaSaadiNoor"))