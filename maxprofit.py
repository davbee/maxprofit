"""
Meta coding interview question on 2024-08-06

Given: a list of randomly generated number simulating predicted
daily stock prices
Goal: calculate the maximum profit that could be generated
from the prediction

Date: 2024-08-17
"""


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
        profit = max(newblock[1:]) - newblock[0]

        #  append the daily profit to profits for the overall trading period
        profits.append(profit)

    # get max profit from the profits for the entire trading period
    peakprofit = max(profits)

    return peakprofit


if __name__ == "__main__":
    # a list of randomly generated number simulating
    # predicted daily stock prices
    # prices = [random.randint(1, 100) for _ in range(10)]
    prices = [10, 9, 16, 17, 19, 23]
    # prices = [8, 6, 5, 4, 3, 2, 1]
    print(prices)
    maxProfit = maxprofit(prices)
    print(maxProfit)
