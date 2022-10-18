"""
https://www.hackerrank.com/challenges/collections-counter/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
"""

'''
    NOT DONE!
'''
from collections import Counter

# no_of_shoes = int(input())
# print(no_of_shoes)
# shoes_in_shop = list(map(int, input().replace(" ", "")))
# print(shoes_in_shop)
no_of_customers = int(input())
for i in range(no_of_customers):
    shoe_price = map(int, input().replace(" ", ""))

print(Counter(shoe_price))
