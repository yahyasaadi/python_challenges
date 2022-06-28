def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


print(to_camel_case("the_stealth_weapon"))
print(to_camel_case("the-stealth-weapon"))

