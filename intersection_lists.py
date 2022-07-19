"""Number 160: Intersection of two linked Lists"""
from Util import ListNode
from Util import create_two_lists


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    l1, l2 = head_a, head_b
    while l1 != l2:
        l1 = l1.next if l1 else head_b
        l2 = l2.next if l2 else head_a

    return l1


input_head_a, input_head_b, expected = create_two_lists([2, 6, 4], [3, 5], -1)
print(get_intersection_node(input_head_a, input_head_b))

