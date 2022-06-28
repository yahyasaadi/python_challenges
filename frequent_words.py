# use the Counter module
from collections import Counter
# use the regex module
import re


def top_3_words(text):
    # count the input, pass through a regex and lowercase it
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    # return the `most common` 3 items
    return [w for w,_ in c.most_common(3)]

print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  , e   .. "))
print(top_3_words("wont won't won't"))