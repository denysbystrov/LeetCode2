"""Number 94: Binary in order traversal"""
from typing import List
from Util import TreeNode


def in_order_traversal(root: TreeNode) -> List[int]:
    stack = []
    elements_traversed = []
    current_node = root
    while current_node is not None or len(stack) > 0:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        elements_traversed.append(current_node.val)
        current_node = current_node.right

    return elements_traversed



