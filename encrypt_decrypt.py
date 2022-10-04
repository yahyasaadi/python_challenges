from string import ascii_lowercase as low

def encrypt(word, n):
    w = [low.index(c) + 1 for c in word]
    for _ in range(n):
        w = [x * 3 - 5 for x in w]
    return w

def decrypt(encrypted_word, n):
    for _ in range(n):
        encrypted_word = [(x + 5) // 3 for x in encrypted_word]
    return "".join(low[c - 1] for c in encrypted_word)


# print(encrypt('abc', 1))
print(decrypt('hahscvhd', 1))