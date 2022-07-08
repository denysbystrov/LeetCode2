from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_dict(root_num: int, node_dict: dict):
    if root_num is None:
        return None
    root_node = TreeNode(root_num)
    queue = [root_node]
    while len(queue) > 0:
        current_node = queue.pop(0)
        left_num, right_num = node_dict[current_node.val][0], node_dict[current_node.val][1]
        if left_num is not None:
            left_node = TreeNode(left_num)
            current_node.left = left_node
            queue.append(left_node)
        if right_num is not None:
            right_node = TreeNode(right_num)
            current_node.right = right_node
            queue.append(right_node)

    return root_node


def create_tree_from_array(array: List) -> TreeNode:
    tree = []
    for num in array:
        new_node = TreeNode(num)
        tree.append(new_node)

    for i in range(len(array)):
        left_child_index = i*2 + 1
        right_child_index = i*2 + 2
        tree[i].left = tree[left_child_index] if left_child_index < len(tree) else None
        tree[i].right = tree[right_child_index] if right_child_index < len(tree) else None

    if len(tree) > 0:
        return tree[0]
    else:
        return None
