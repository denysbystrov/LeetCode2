"""Number 101: symmetric tree"""
from Util import TreeNode
from Util import create_tree_from_array


def is_symmetric(root: TreeNode) -> bool:
    lhs_queue = [root.left] if root.left else []
    rhs_queue = [root.right] if root.right else []

    while len(lhs_queue) > 0 and len(rhs_queue) > 0:
        left_val = lhs_queue.pop(0)
        right_val = rhs_queue.pop(0)
        if left_val is not None and right_val is not None:
            if left_val.val != right_val.val:
                return False
        elif left_val != right_val:
            return False
        if left_val is not None:
            lhs_queue.append(left_val.left)
            lhs_queue.append(left_val.right)
        if right_val is not None:
            rhs_queue.append(right_val.right)
            rhs_queue.append(right_val.left)

    return len(lhs_queue) == len(rhs_queue)


array1 = [1, 2, 2, 3, 4, 4, 3, 5, None, None, None, None, None, None, 5]
root_input = create_tree_from_array(array1)
print(is_symmetric(root_input))
