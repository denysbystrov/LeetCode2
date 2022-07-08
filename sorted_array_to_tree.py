"""Number 108: convert sorted array to binary search tree"""
from typing import List
from Util import TreeNode


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    def sorted_to_bst_rec(left_pointer, right_pointer):
        if left_pointer == right_pointer:
            return TreeNode(nums[left_pointer])
        if left_pointer > right_pointer:
            return None
        mid = int((left_pointer+right_pointer)/2)
        node = TreeNode(nums[mid])
        node.left = sorted_to_bst_rec(left_pointer, mid-1)
        node.right = sorted_to_bst_rec(mid+1, right_pointer)
        return node

    return sorted_to_bst_rec(0, len(nums)-1)
