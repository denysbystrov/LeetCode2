from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_array(root_num: int, node_dict: dict):
    if root_num is None:
        return None
    root_node = TreeNode(root_num)
    queue = [root_node]
    while len(queue) > 0:
        current_node = queue.pop(0)
        left_num, right_num = node_dict[current_node.val][0], node_dict[current_node.val][0]
        if left_num is not None:
            left_node = TreeNode(left_num)
            current_node.left = left_node
            queue.append(left_node)
        if right_num is not None:
            right_node = TreeNode(right_num)
            current_node.right = right_node
            queue.append(right_node)

    return root_node
