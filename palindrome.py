def palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

print("Is 22022022 a palindrome?", palindrome(22022022))
