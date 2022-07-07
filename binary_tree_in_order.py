"""Number 94: Binary in order traversal"""
from typing import List
from Util import TreeNode
from Util import create_tree_from_array


def in_order_traversal(root: TreeNode) -> List[int]:
    def in_order_traversal_rec(node):
        if node is None:
            return []
        return in_order_traversal_rec(node.left) + [node.val] + in_order_traversal_rec(node.right)

    return in_order_traversal_rec(root)
