from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


def build_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(s.removeNthFromEnd(build_list([1]), 1)) == []
    assert to_list(s.removeNthFromEnd(build_list([1, 2]), 1)) == [1]
    assert to_list(s.removeNthFromEnd(build_list([1, 2]), 2)) == [2]
