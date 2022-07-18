"""Number 141: Linked List Cycle"""
from Util import ListNode
from Util import create_list_from_array


def has_cycle(head: ListNode) -> bool:
    node_set = set()
    current_node = head
    while current_node:
        if current_node in node_set:
            return True
        node_set.update([current_node])
        current_node = current_node.next

    return False


head_node = create_list_from_array([1, 2, 3, 4], -1)
print(has_cycle(head_node))
