"""Number 121: Best time to buy and sell stock"""
from typing import List


def max_profit(prices: List[int]) -> int:
    max_p = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
        else:
            l = r
        r += 1
    return max_p


print(max_profit([4, 3, 2, 1, 0]))
