"""Number 104: Maximum Depth of Binary Tree"""
from Util import TreeNode


def maximum_depth(root: TreeNode) -> int:

    def max_depth_rec(node) -> int:
        if node is None:
            return 0

        left_depth = max_depth_rec(node.left)
        right_depth = max_depth_rec(node.right)
        return 1 + max(left_depth, right_depth)

    return max_depth_rec(root)
