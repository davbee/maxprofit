"""
Meta coding interview question on 2024-08-06

Given: a list of randomly generated number simulating predicted
daily stock prices
Goal: calculate the maximum profit that could be generated
from the prediction

Date: 2024-08-17
"""

import random

# a list of randomly generated number simulating predicted daily stock prices
numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

# number = random.choice(numbers)
# print(number)

profits = []
for i in range(len(numbers) - 1):
    # create a new slice
    newBlock = numbers[i:]
    # profits = max of the new slide minus the stock market
    # entry point for the day
    profit = max(newBlock) - newBlock[0]
    #  append the daily profit to profits for the overall trading period
    profits.append(profit)

# get max profit from the profits for the entire trading period
maxProfit = max(profits)
print(maxProfit)
