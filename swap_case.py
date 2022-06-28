def swap_case(s):
        new_s = "".join(s[i].lower() if s[i].isupper() else s[i].upper() for i in range(len(s)))
        return new_s
        

# swap_case("Yahya")
print(swap_case('HackerRank.com presents "Pythonist 2".'))