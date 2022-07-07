"""Number 94: Binary in order traversal"""
from typing import List
from Util import TreeNode
from Util import create_tree_from_array


def in_order_traversal(root: TreeNode) -> List[int]:
    stack = [root]
    elements_traversed = []
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node is None:
            continue
        left_child = current_node.left
        right_child = current_node.right
        current_node.left = None
        current_node.right = None
        if left_child is None and right_child is None:
            elements_traversed.append(current_node.val)
        else:
            stack.append(right_child)
            stack.append(current_node)
            stack.append(left_child)

    return elements_traversed



