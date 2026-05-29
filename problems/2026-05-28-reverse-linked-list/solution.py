from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


def build_list(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseList(build_list([1, 2, 3]))) == [3, 2, 1]
    assert to_list(s.reverseList(build_list([1, 2]))) == [2, 1]
    assert to_list(s.reverseList(build_list([1]))) == [1]
    assert to_list(s.reverseList(build_list([]))) == []
