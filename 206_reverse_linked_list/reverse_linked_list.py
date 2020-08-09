from singly_linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        second_node = head.next
        new_head = self.reverseList(second_node)
        second_node.next = head
        head.next = None
        return new_head

    def reverseListIterative(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # There are at least 2 nodes
        curr_node = head.next
        prev_node = head
        while curr_node.next is not None:
            # At least 3 nodes
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        # Finish up by letting the last node in the list point at its predecessor
        curr_node.next = prev_node
        # The original head is the last node now
        head.next = None
        return curr_node
