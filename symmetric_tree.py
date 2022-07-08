"""Number 101: symmetric tree"""
from Util import TreeNode
from Util import create_tree_from_array


def is_symmetric(root: TreeNode) -> bool:
    def is_symmetric_rec(left_node: TreeNode, right_node: TreeNode):
        if left_node is None or right_node is None:
            return left_node == right_node
        if left_node.val == right_node.val:
            return is_symmetric_rec(left_node.left, right_node.right) and is_symmetric_rec(left_node.right,
                                                                                           right_node.left)
        else:
            return False

    return is_symmetric_rec(root.left, root.right)


array1 = [1, 2, 2, 3, 4, 4, 3, 5, None, None, None, None, None, None, 5]
root_input = create_tree_from_array(array1)
print(is_symmetric(root_input))
