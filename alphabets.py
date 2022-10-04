# alpha = 'abcdefghijklmnopqrstuvwxyz'
# lst_alpha = list(alpha)

# alpha_dict = {}

# for i in range(1, 27):
#     alpha_dict.update({lst_alpha[i-1]:i})

# print(alpha_dict)
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
key_list = list(alphabet.keys())
val_list = list(alphabet.values())
print(key_list[val_list.index(1)])

def encrypt(word, n):
    # Happy coding!
    lst_word = list(word)

    for i in range(len(lst_word)):
        lst_word[i] = alphabet[lst_word[i]]

    for j in range(n):
        lst_word = [x * 3 - 5 for x in lst_word]

    return lst_word

def encrypt(word):
    # Happy coding!
    lst_word = list(word)

    for i in range(len(lst_word)):
        lst_word[i] = alphabet[lst_word[i]]

    return lst_word

def decrypt(encrypted_word, n):
    for _ in range(n):
        encrypted_word = [(x + 5) // 3 for x in encrypted_word]
    
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())

    return ''.join(key_list[val_list.index(i)] for i in encrypted_word)


# print(encrypt('abc'))
# print(encrypt('test', 6))

print(decrypt([7, 115, 16, 61, 106, 43], 2))

