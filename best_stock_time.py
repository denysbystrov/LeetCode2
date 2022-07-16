"""Number 121: Best time to buy and sell stock"""
from typing import List


def max_profit(prices: List[int]) -> int:
    current_pointer = 1
    buy_pointer = 0
    sell_pointer = 0
    total_profit = 0
    while current_pointer < len(prices):
        if total_profit == 0:
            if prices[current_pointer] > prices[buy_pointer]:
                sell_pointer = current_pointer
            else:
                buy_pointer = current_pointer
                sell_pointer = current_pointer
        else:
            for i in range(sell_pointer+1, current_pointer):
                if prices[i] < prices[buy_pointer]:
                    if prices[current_pointer] - prices[i] >= total_profit:
                        buy_pointer = i
                        sell_pointer = current_pointer
            if prices[sell_pointer] <= prices[current_pointer]:
                sell_pointer = current_pointer

        total_profit = prices[sell_pointer] - prices[buy_pointer]
        current_pointer += 1

    return total_profit


print(max_profit([4, 3, 2, 1, 0]))
