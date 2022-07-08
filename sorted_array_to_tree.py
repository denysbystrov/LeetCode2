"""Number 108: convert sorted array to binary search tree"""
from typing import List
from Util import TreeNode


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    if len(nums) == 0:
        return None
    mid = int(len(nums)/2)
    node = TreeNode(nums[mid])
    node.left = sorted_array_to_bst(nums[:mid])
    node.right = sorted_array_to_bst(nums[mid+1:])
    return node
