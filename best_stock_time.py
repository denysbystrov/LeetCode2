"""Number 121: Best time to buy and sell stock"""
from typing import List


def max_profit(prices: List[int]) -> int:
    highest_profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > highest_profit:
                highest_profit = prices[j] - prices[i]

    return highest_profit


print(max_profit([2, 1, 2, 0, 1]))
