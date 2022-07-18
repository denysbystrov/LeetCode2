"""Number 141: Linked List Cycle"""
from Util import ListNode
from Util import create_list_from_array


def has_cycle(head: ListNode) -> bool:
    pointer1 = head
    pointer2 = head.next if head.next else None
    count = 0
    while pointer1 and pointer2:
        if pointer1 == pointer2:
            return True
        if count % 2 == 0:
            pointer1 = pointer1.next
        pointer2 = pointer2.next
        count += 1

    return False
