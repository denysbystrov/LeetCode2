"""Number 141: Linked List Cycle"""
from Util import ListNode
from Util import create_list_from_array


def has_cycle(head: ListNode) -> bool:
    pointer1 = head
    pointer2 = head
    while pointer2 and pointer2.next:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
        if pointer1 == pointer2:
            return True

    return False
