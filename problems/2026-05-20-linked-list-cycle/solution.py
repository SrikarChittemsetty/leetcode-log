from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def build_list(values, pos=-1):
    if not values:
        return None

    nodes = [ListNode(value) for value in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    s = Solution()
    assert s.hasCycle(build_list([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(build_list([1, 2], 0)) is True
    assert s.hasCycle(build_list([1], -1)) is False
    assert s.hasCycle(build_list([], -1)) is False
    assert s.hasCycle(build_list([1, 2, 3, 4], -1)) is False
