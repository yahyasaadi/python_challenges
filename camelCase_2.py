"""
    https://www.codewars.com/kata/517abf86da9663f1d2000003
"""

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


print(to_camel_case("the_stealth_weapon"))
print(to_camel_case("the-stealth-weapon"))

