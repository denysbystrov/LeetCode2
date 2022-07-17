"""Number 136: Single Number"""
from typing import List


def single_number(nums: List[int]) -> int:
    final_num = 0
    for num in nums:
        final_num = final_num ^ num
    return final_num
