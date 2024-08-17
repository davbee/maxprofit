"""
Meta coding interview question on 2024-08-06

Given: a list of randomly generated number simulating predicted
daily stock prices
Goal: calculate the maximum profit that could be generated
from the prediction

Date: 2024-08-17
"""

import random

# number = random.choice(numbers)
# print(number)


def maxprofit(numbers: list) -> int:
    """
    calculate the maximum profit that could be generated
    from the prediction
    """
    profits = []
    for i in range(len(numbers) - 1):
        # create a new slice
        newblock = numbers[i:]

        # profits = max of the new slide minus the stock market
        # entry point for the day
        profit = max(newblock) - newblock[0]

        #  append the daily profit to profits for the overall trading period
        profits.append(profit)

    # get max profit from the profits for the entire trading period
    peakprofit = max(profits)

    return peakprofit


if __name__ == "__main__":
    # a list of randomly generated number simulating
    # predicted daily stock prices
    prices = [random.randint(1, 100) for _ in range(10)]
    print(prices)
    maxProfit = maxprofit(prices)
    print(maxProfit)
