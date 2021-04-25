import pytest
from singly_linked_list import ListNode, make_linked_list, print_linked_list, linked_list_as_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        # Neither is empty, both have at least 1 value
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                current = l1
                l1 = l1.next
            else:
                current.next = l2
                current = l2
                l2 = l2.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return head

    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        merged_head = self.mergeTwoListsRecursive(l1, l2)
        head.next = merged_head
        return head
        

test_data_set = [
    ([], [], []),
    ([], [0], [0]),
    ([1, 2, 15], [10, 12, 16], [1, 2, 10, 12, 15, 16]),
    ([1, 3, 4], [1, 2, 3], [1, 1, 2, 3, 3, 4]),
]

@pytest.mark.parametrize('l1, l2, expected', test_data_set)
def test_solution(l1, l2, expected):
    l1 = make_linked_list(l1)
    l2 = make_linked_list(l2)
    solution = Solution()
    merged_lists = solution.mergeTwoListsRecursive(l1, l2)
    assert expected == linked_list_as_list(merged_lists)
