"""Number 104: Maximum Depth of Binary Tree"""
from Util import TreeNode


def maximum_depth(root: TreeNode) -> int:
    if root:
        root.val = 1
    queue = [root]
    max_depth = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node is not None:
            max_depth = max(current_node.val, max_depth)
            if current_node.left is not None:
                current_node.left.val = current_node.val + 1
            if current_node.right is not None:
                current_node.right.val = current_node.val + 1
            queue.append(current_node.left)
            queue.append(current_node.right)

    return max_depth
