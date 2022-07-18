"""Number 160: Intersection of two linked Lists"""
from Util import ListNode
from Util import create_two_lists


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    def find_list_length(node: ListNode) -> int:
        current_node = node
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next

        return length

    length_a = find_list_length(head_a)
    length_b = find_list_length(head_b)

    while length_a != length_b:
        if length_b > length_a:
            head_b = head_b.next
            length_b -= 1
        else:
            head_a = head_a.next
            length_a -= 1

    while head_a != head_b:
        head_a = head_a.next
        head_b = head_b.next

    return head_a


input_head_a, input_head_b, expected = create_two_lists([1, 2, 3, 4, 5], [6, 7, 8], 2)
print(get_intersection_node(input_head_a, input_head_b))

